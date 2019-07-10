import os
import redis
import datetime
import requests



class Crawler():
    def __init__(self, root, prefix="", postfix=""):
        self.root = root
        self.prefix = prefix
        self.postfix = postfix

        self.requests = 0

    def _check_url(self, url):
        self.requests += 1

        if requests.head(url).status_code == 200:
            return True
        else:
            return False

    def search(self, year, month, timetable=[[0, 24]]):
        main_url = self.root + self.prefix + str(year).zfill(2) + str(month).zfill(2)

        for ranges in timetable:
            for timestamps in [(days, hours, minutes)
                                for days in range(31, 1, -1)
                                for hours in range(ranges[0], ranges[1])
                                for minutes in range(0, 60)]:

                url = (main_url + str(timestamps[0]).zfill(2)
                                + str(timestamps[1]).zfill(2)
                                + str(timestamps[2]).zfill(2)
                                + self.postfix)

                if self._check_url(url):
                    return url

        raise Exception("Couldn't find file on remote server!")


def get_config(config={}):
    config["ROOT_URL"] = os.environ["ROOT_URL"]

    config["REDIS_HOSTNAME"] = os.environ.get("REDIS_HOSTNAME") or "redis"
    config["REDIS_KEY"] = os.environ.get("REDIS_KEY") or "url"

    config["YEAR"] = os.environ.get("YEAR") or datetime.datetime.today().year
    config["MONTH"] = os.environ.get("MONTH") or datetime.datetime.today().month

    config["TIMETABLE"] = [[6, 17], [17, 25], [0, 6]]

    return config

def main():
    config = get_config()

    crawler = Crawler(config["ROOT_URL"], postfix=".xlsx")

    try:
        result = crawler.search(config["YEAR"], config["MONTH"], config["TIMETABLE"])

        db = redis.Redis(host=config["REDIS_HOSTNAME"], port=6379, decode_responses=True)
        db.set(config["REDIS_KEY"], result)
    except:
        pass


if __name__ == "__main__":
    main()
