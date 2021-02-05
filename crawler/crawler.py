#!/usr/bin/env python
import redis
import requests

import config
import logging

"""Initialize logger."""
log = logging.getLogger()

log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


class Crawler():
    def __init__(self, root, prefix="", postfix=""):
        """Simple Web Crawler.

        Attributes:
            root (str): URL to with root directory.
            prefix (str): Prefix of file.
            postfix (str): Postfix or extension of file.

            requests (int): Returns number off all requests made.
        """
        self.root = root
        self.prefix = prefix
        self.postfix = postfix

        self.requests = 0


    def _check_url(self, url):
        """Checks for file on remote server."""
        self.requests += 1
        log.debug("Crawler: Checking {} !".format(url))

        if requests.head(url).status_code == 200:
            return True
        else:
            return False


    def search(self, year, month, timetable=[[0, 24]]):
        """Gets url to file on remote server.

        Loops throught all posible datetime combinations in filename.
        Needs year and month, generates time itself.

        Args:
            year (int): Year in filename.
            month (int): Month in filename.
            timetable (list, optional): List of lists with best hour ranges to search.

        Returns:
            URL when found, None when not.
        """
        main_url = self.root + self.prefix + str(year).zfill(2) + str(month).zfill(2)
        log.debug("Crawler: {}".format(main_url))

        for ranges in timetable:
            log.info("Crawler: Checking for range {} - {}.".format(ranges[0], ranges[1]))

            for timestamps in [(days, hours, minutes)
                                for days in range(31, 0, -1)
                                for hours in range(ranges[0], ranges[1])
                                for minutes in range(0, 60)]:

                url = (main_url + str(timestamps[0]).zfill(2)
                                + str(timestamps[1]).zfill(2)
                                + str(timestamps[2]).zfill(2)
                                + self.postfix)

                if self._check_url(url):
                    return url

        return None


def main():
    """Searches for and sets found URL in database."""
    conf = config.Config()

    log.info("Initialized crawling job for {} month.".format(conf.month))

    crawler = Crawler(conf.root_url, postfix=".xlsx")
    log.warning("Starting! Crawling in {}...".format(crawler.root))

    results = crawler.search(conf.year, conf.month, conf.timetable)

    if results is None:
        log.critical("Crawler didn't found anything! Exiting...")
        exit(1)

    else:
        log.warning("Found file: {} ! After {} requests.".format(results, crawler.requests))

        try:
            log.info("Connecting to Redis database...")

            db = redis.Redis(host=conf.redis_hostname, port=6379, decode_responses=True)
            db.set("url:{}".format(conf.month), results)

            log.warning("Success! Key url:{} set to {} ! Exiting...".format(conf.month, results))

        except:
            log.critical("Error while setting Redis key!")
            exit(1)



if __name__ == "__main__":
    main()
