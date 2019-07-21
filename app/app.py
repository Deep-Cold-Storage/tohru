import json
import redis
from datetime import datetime, timedelta
from flask import Flask, Response, request

import config


app = Flask(__name__)

conf = config.Config()
database = redis.Redis(host=conf.redis_hostname, port=6379, decode_responses=True)


class Origin():
    def __init__(self, id):
        self.id = id
        self.name = database.get("origin:{}:name".format(self.id))

        self.longitude, self.latitude = database.geopos("origins:positions", self.id)[0]

        self.connections = [key.split(":")[3] for key in database.keys("origin:{}:destination:*:duration".format(self.id))]

    def json(self):
        json = {"name": self.name, "longitude": self.longitude, "latitude": self.latitude, "connections": self.connections}

        return json


def json_response(payload, status=200):
    if status >= 200 and status < 300:
        envelope = {"status": "success",
                    "payload": payload}
    else:
        envelope = {"status": "error",
                    "message": payload}

    return Response(json.dumps(envelope, ensure_ascii=False), status=status, mimetype="application/json")


def get_now():
    now = datetime.today().replace(month=6, day=29)
    return now


def retrieve_origins():
    origins_ids = [key.split(":")[1] for key in database.keys("origin:*:name")]
    return origins_ids


def retrieve_destinations(origin_id):
    destinations_ids = [key.split(":")[3] for key in database.keys("origin:{}:destination:*:duration".format(origin_id))]
    return destinations_ids


def calculate_until(departure, now):
    time = datetime.strptime(departure, "%H:%M").replace(now.year, now.month, now.day)
    until = time - now

    return int(until.seconds / 60)


def calculate_arrival(departure, duration, now):
    time = datetime.strptime(departure, "%H:%M").replace(now.year, now.month, now.day)
    arrival = time + timedelta(minutes=int(duration))

    return arrival.strftime("%H:%M")


def sort_departures(departures, now):
    past = []
    future = []

    for departure in departures:
        departure_time = datetime.strptime(departure, "%H:%M").replace(now.year, now.month, now.day)
        if departure_time > now:
            future.append(departure)
        else:
            past.append(departure)

    return past, future


def verify_activity(origin_id, now):
    for destination_id in retrieve_destinations(origin_id):
        date = now.strftime("%d.%m.%Y")

        departures_now = database.get("origin:{}:destination:{}:date:{}".format(origin_id, destination_id, date))

        if departures_now is None:
            continue
        else:
            departures_now = json.loads(departures_now)

        past_departures, future_departures = sort_departures(departures_now, now)

        if not future_departures:
            return False
        else:
            return True


@app.route("/origins/")
def origins():
    response = {}

    for origin_id in retrieve_origins():
        response[origin_id] = Origin(origin_id).json()

    return json_response(response, 200)


@app.route("/origins/<origin_id>/")
def origin(origin_id):
    response = {}

    if origin_id in retrieve_origins():
        response["origin_id"] = Origin(origin_id).json()

        return json_response(response)
    else:
        return json_response("Origin with specified id doesn't exist!", 404)


@app.route("/origins/geo/")
def origin_geo():
    lng = request.args.get("lng")
    lat = request.args.get("lat")

    active = request.args.get("active")

    if lat is None or lng is None:
        return json_response("You must provide ?lat and ?lng query params!", 400)

    nearest_origins = database.georadius("origins:positions", lng, lat, 1000, unit="km", sort="ASC")

    if nearest_origins is None:
        return json_response("You're probably too far from any origins!", 400)

    response = {}

    if active is not None and active.upper() == "TRUE":
        now = get_now()

        for origin_id in nearest_origins:
            if verify_activity(origin_id, now):

                response[origin_id] = Origin(origin_id).json()
                return json_response(response)

        return json_response("Couldn't find any active origins nearby!", 404)

    else:
        response[nearest_origins[0]] = Origin(nearest_origins[0]).json()
        return json_response(response)


@app.route("/schedules/")
def schedules():
    origin = request.args.get("origin")
    destination = request.args.get("destination")

    if origin is None or destination is None:
        return json_response("You must provide ?origin and ?destination query params!", 400)

    try:
        offset = int(request.args.get("offset") or "0")
    except ValueError:
        return json_response("Offset must be an integer!", 400)

    if offset < 0:
        return json_response("You can't requests schedules with offset < 0!", 400)

    now = get_now() + timedelta(days=offset)
    date = now.strftime("%d.%m.%Y")

    departures = database.get("origin:{}:destination:{}:date:{}".format(origin, destination, date))
    if departures is None:
        return json_response("Couldn't find any departures for {}!".format(date), 404)
    else:
        departures = json.loads(departures)

    duration = database.get("origin:{}:destination:{}:duration".format(origin, destination))
    arrivals = [calculate_arrival(departure, duration, now) for departure in departures]

    response = {"date": date,
                "offset": offset,
                "origin": origin,
                "destination": destination}

    sorted = request.args.get("sorted")
    if sorted is not None and sorted.upper() == "TRUE":
        past_departures, future_departures = sort_departures(departures, now)

        response["departures"] = {"past": past_departures, "future": future_departures}
    else:
        response["departures"] = departures
        response["arrivals"] = arrivals

    return json_response(response)


@app.route("/live/")
def live():
    origin = request.args.get("origin")
    destination = request.args.get("destination")

    if origin is None or destination is None:
        return json_response("You must provide ?origin and ?destination query params!", 400)

    now = get_now()
    date = now.strftime("%d.%m.%Y")

    departures = database.get("origin:{}:destination:{}:date:{}".format(origin, destination, date))
    if departures is None:
        return json_response("Couldn't find any departures for {}!".format(date), 404)
    else:
        departures = json.loads(departures)

    response = {"date": date,
                "origin": origin,
                "destination": destination}

    past_departures, future_departures = sort_departures(departures, now)

    if not future_departures:
        return json_response("Couldn't find any more departures for {} at this time!".format(date), 404)

    duration = database.get("origin:{}:destination:{}:duration".format(origin, destination))

    response["departure"] = future_departures[0]
    response["until"] = calculate_until(future_departures[0], now)
    response["arrival"] = calculate_arrival(future_departures[0], duration, now)

    return json_response(response)


if __name__ == "__main__":
    app.run(debug=True)
