import os


class Config:
    def __init__(self):
        self.redis_hostname = os.environ.get("REDIS_HOSTNAME") or "redis"
        self.month = os.environ.get("MONTH")
