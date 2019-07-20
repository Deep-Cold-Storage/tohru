import json
import redis
from datetime import datetime, timedelta
from flask import Flask, Response, request

import config


app = Flask(__name__)

conf = config.Config()
database = redis.Redis(host=conf.redis_hostname, port=6379, decode_responses=True)


class Origin():
    def __init__(self, code):
        self.code = code
        self.name = database.get("origin:{}:name".format(self.code))

        self.longitude, self.latitude = database.geopos("origins:positions", self.code)[0]

        self.connections = [key.split(":")[3] for key in database.keys("origin:{}:destination:*:duration".format(self.code))]

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
        try:
            departures_now = json.loads(database.get(
                                "origin:{}:destination:{}:date:{}".format(
                                    origin_id, destination_id, now.strftime("%d.%m.%Y"))))
        except TypeError:
            continue

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

    offset = int(request.args.get("offset") or "0")

    if offset < 0:
        return json_response("You can't requests schedules with offset < 0!", 404)

    now = get_now() + timedelta(days=offset)
    try:
        departures = json.loads(database.get(
                                    "origin:{}:destination:{}:date:{}".format(
                                        origin, destination, now.strftime("%d.%m.%Y"))))
    except TypeError:
        return json_response("Couldn't find any departures for {}!".format(now.strftime("%d.%m.%Y")), 404)

    response = {"date": now.strftime("%d.%m.%Y"),
                "offset": offset,
                "origin": origin,
                "destination": destination}

    sorted = request.args.get("sorted")
    if sorted is not None and sorted.upper() == "TRUE":
        past_departures, future_departures = sort_departures(departures, now)

        response["departures"] = {"past": past_departures, "future": future_departures}

    else:
        response["departures"] = departures

    return json_response(response)


@app.route("/live/")
def live():
    origin = request.args.get("origin")
    destination = request.args.get("destination")

    if origin is None or destination is None:
        return json_response("You must provide ?origin and ?destination query params!", 400)

    now = get_now()

    try:
        departures = json.loads(database.get(
                                    "origin:{}:destination:{}:date:{}".format(
                                        origin, destination, now.strftime("%d.%m.%Y"))))
    except TypeError:
        return json_response("Couldn't find any departures for {}!".format(now.strftime("%d.%m.%Y")), 404)

    response = {"date": now.strftime("%d.%m.%Y"),
                "origin": origin,
                "destination": destination}

    past_departures, future_departures = sort_departures(departures, now)

    departure_time = datetime.strptime(future_departures[0], "%H:%M").replace(now.year, now.month, now.day)
    departure_timedelta = departure_time - now

    departure_minutes = int(departure_timedelta.seconds / 60)

    response["until"] = departure_minutes
    response["departure"] = future_departures[0]
    response["arrival"] = (departure_time + timedelta(minutes=int(database.get("origin:{}:destination:{}:duration".format(origin, destination))))).strftime("%H:%M")

    return json_response(response)


if __name__ == "__main__":
    app.run(debug=True)
