# Tohru - Parser
[![Build Status](https://drone.bednarski.dev/api/badges/RangerDigital/tohru-parser/status.svg)](https://drone.bednarski.dev/RangerDigital/tohru-parser)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


**Tohru** is a simple **Progressive Web App** created to streamline getting between my university campuses via private bus.

>You can find out more at [Tohru Official Website](https://tohru.bednarski.dev).

The whole architecture is made from microservices and batch jobs running in **Docker** containers.

**Tohru - Parser** gets the **URL** to latest file from Redis and downloads It. Then parses columns containing departure times of buses. Saves It in Redis database with expiration dates.

## Usage

>This project is hardcoded to my particular problem, you probably won't find it useful.

**Docker Container** available via DockerHub:
```
rangerdigital/tohru-parser:latest
```

**Environment Variables:**
- **REDIS_HOSTNAME** - _(Optional)_ Redis instance hostname/address. Default: **redis**
- **FILENAME** - _(Optional)_ Name of file used for parsing. Default: **timetable.xlsx**
- **MONTH** - _(Optional)_ Month used for URL retrieval from Redis.
- **EXPIRE** - _(Optional)_ Set expiration date on key. Default: **True**

## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
