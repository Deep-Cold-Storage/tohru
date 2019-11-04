# Tohru - Parser
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


**Tohru** is a simple **Progressive Web App** created to streamline getting between my university campuses via private bus.

>You can find out more at [Tohru Official Website](https://tohru.bednarski.dev).

The whole architecture is made from microservices and batch jobs running in **Docker** containers.

**Tohru - Parser** gets the **URL** to latest file from Redis and downloads It.

After that, It gets information about origins/stations from YAML file. _(This file can be replaced by mounting volume to the container.)_

- **Routes**

    Then It parses columns containing departure times of buses. Saves them in Redis database with expiration dates.

- **Origins**

    Saves metadata about origins, name, and geohash with origin position in Redis database.


## Usage

>This project is hardcoded to my particular problem, you probably won't find it useful.

**Docker Container** available via DockerHub:
```
rangerdigital/tohru-parser:latest
```

**Environment Variables:**
- **REDIS_HOSTNAME** - _(Optional)_ Redis instance hostname/address. Default: **redis**
- **FILENAME** - _(Optional)_ Name of file used for parsing. Default: **timetable.xlsx**
- **YAML_PATH** - _(Optional)_ Name of YAML file with origins data. Default: **data/origins.yaml**
- **MONTH** - _(Optional)_ Month used for URL retrieval from Redis.
- **EXPIRE** - _(Optional)_ Set expiration date on key. Default: **True**

## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
