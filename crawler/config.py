import os
from datetime import datetime

class Config:
    def __init__(self):
        """Tohru Crawler configuration.

        Gets config from Docker container environment variables.
        """
        self.root_url = os.environ["ROOT_URL"]
        self.timetable = [[6, 17], [17, 25], [0, 6]]

        self.redis_hostname = os.environ.get("REDIS_HOSTNAME") or "redis"

        self.year = os.environ.get("YEAR") or datetime.today().year
        self.month = os.environ.get("MONTH") or datetime.today().month
