import os
from datetime import datetime

class Config:
    def __init__(self):
        """Tohru App configuration.

        Gets config from Docker container environment variables.
        """
        self.redis_hostname = os.environ.get("REDIS_HOSTNAME") or "redis"
        
        self.month = os.environ.get("MONTH")
