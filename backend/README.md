# Tohru - Backend

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**Tohru** is a simple **Progressive Web App** created to streamline getting between my university campuses via private bus.

> You can find out more at [Tohru Official Website](https://tohru.bednarski.dev).

The whole architecture is made from microservices and batch jobs running in **Docker** containers.

**Tohru - Backend** serves live data about routes and buses via RESTful API.

## Usage

> This project is hardcoded to my particular problem, you probably won't find it useful.

**Docker Container** available via DockerHub:

```
rangerdigital/tohru:latest
```

**Environment Variables:**

- **MONTH** - _(Optional)_ Month used by the server for development.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
