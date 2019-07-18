import os
from datetime import datetime

class Config:
    def __init__(self):
        """Tohru Parser configuration.

        Gets config from Docker container environment variables.
        """
        self.redis_hostname = os.environ.get("REDIS_HOSTNAME") or "redis"
        self.redis_hostname = "192.168.5.1"

        self.filename = os.environ.get("FILENAME") or "timetable.xlsx"
        self.month = os.environ.get("MONTH") or datetime.today().month
