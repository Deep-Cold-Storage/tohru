#!/usr/bin/env python
import redis
import requests
import openpyxl

import json
import logging
from datetime import datetime, timedelta

import config

"""Initialize logger."""
log = logging.getLogger()

log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


class Route():
    def __init__(self, origin, destination, duration, timetable):
        self.origin = origin
        self.duration = duration
        self.destination = destination

        self.timetable = timetable

    def store(self, database, expire=True):
        root_key = ("origin:{}:destination:{}".format(self.origin, self.destination))

        database.set(root_key + ":duration", self.duration)
        log.debug("Set duration to: {}".format(self.duration))

        for days in self.timetable:
            key = root_key + ":date:{}".format(days)
            value = json.dumps(self.timetable[days])
            expiration = datetime.strptime(days, "%d.%m.%Y") + timedelta(days=1)

            database.set(key, value)
            log.info("Stored timetable for route {} ---> {},".format(self.origin, self.destination,))
            log.info("Added {} days.".format(len(self.timetable)))

            if expire:
                log.debug("Set expiration on {}.".format(expiration))
                database.expireat(key, expiration)


class DocumentParser():
    def __init__(self, path, sheet=0, start_row=3):
        self.path = path

        self.workbook = openpyxl.load_workbook(self.path)
        self.sheet = self.workbook[self.workbook.sheetnames[sheet]]

        self.start_row = start_row

    def column(self, column):
        departures = {}

        for row in range(self.start_row, self.sheet.max_row + 1):
            date_cell = self.sheet.cell(row=row, column=1)
            data_cell = self.sheet.cell(row=row, column=column)

            if date_cell.value is not None:
                date = date_cell.value.strftime("%d.%m.%Y")
                departures[date] = []

            if data_cell.value is None:
                continue
            else:
                departures[date].append(data_cell.value.strftime("%H:%M"))

        return departures


def download_file(url, filename):
    with open(filename, "wb") as file:
        file.write(requests.get(url).content)


def main():
    conf = config.Config()
    log.info("Initialized parsing job for {} month.".format(conf.month))

    log.info("Connecting to Redis database...")
    database = redis.Redis(host=conf.redis_hostname, port=6379, decode_responses=True)

    try:
        url = database.get("url:{}".format(conf.month))
    except:
        log.critical("URL for {} month not found! Exiting...".format(conf.month))
        exit(1)

    download_file(url, conf.filename)
    log.warning("Success! File downloaded and saved.")

    parser = DocumentParser(conf.filename)
    log.info("Parsing timetable...")

    routes = []

    # Hard-coded routes between stations. Will be replaced by Admin UI.
    routes.append(Route("ctir", "tycz", 10, parser.column(8)))
    routes.append(Route("ctir", "tesc", 20, parser.column(8)))
    routes.append(Route("tycz", "tesc", 10, parser.column(9)))

    routes.append(Route("ofka", "tycz", 30, parser.column(2)))
    routes.append(Route("ofka", "ctir", 40, parser.column(2)))

    routes.append(Route("ciep", "tycz", 20, parser.column(3)))
    routes.append(Route("ciep", "ctir", 30, parser.column(3)))

    routes.append(Route("pows", "tycz", 10, parser.column(4)))
    routes.append(Route("pows", "ctir", 20, parser.column(4)))

    routes.append(Route("tesc", "tycz", 10, parser.column(5)))
    routes.append(Route("tesc", "ctir", 20, parser.column(5)))

    routes.append(Route("tycz", "ctir", 10, parser.column(6)))
    # I am ashamed.

    log.info("Storing data in Redis...")
    for route in routes:
        route.store(database, False)

    log.warning("Success! Exiting!")


if __name__ == "__main__":
    main()
