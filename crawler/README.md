# Tohru - Web Crawler
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FRangerDigital%2Ftohru-crawler%2Fbadge&style=flat)](https://actions-badge.atrox.dev/RangerDigital/tohru-crawler/goto)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


**Tohru** is a simple **Progressive Web App** created to streamline getting between my university campuses via private bus.

>You can find out more at [Tohru Official Website](https://tohru.bednarski.dev).

The whole architecture is made from microservices and batch jobs running in **Docker** containers.

**Tohru - Crawler** gets the **URL** to latest file on university server containing a **timetable** for a particular month. This job runs once a month. It loops and tries all possible filenames when found saves the URL in Redis database.

## Usage

>This project is hardcoded to my particular problem, you probably won't find it useful.

**Docker Container** available via DockerHub:
```
rangerdigital/tohru-crawler:latest
```

**Environment Variables:**
- **ROOT_URL** - Root URL of the directory containing timetable file.
- **REDIS_HOSTNAME** - _(Optional)_ Redis instance hostname/address. Default: **redis**
- **YEAR** - _(Optional)_ Year used in the filename when searching.
- **MONTH** - _(Optional)_ Month used in the filename when searching.

## FAQ

- **Why not use the Async library for making multiple requests?**

It needs to be done once a month, time is not a problem. It also could be slowed down by rate-limiting on the remote server. Simplicity was the most important factor.

- **Why not use web scraping and get the URL via the student portal UI?**

It would be faster, but I would need to store and use my credentials. It is always a security concern. Also, any change to Web UI would force me to change scraping logic.


## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
