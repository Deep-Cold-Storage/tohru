FROM ubuntu:latest
LABEL Description="Tohru - Crawler"

RUN apt update && apt install -y python3 python3-pip tzdata
RUN pip3 install redis requests

# Changes time zone inside container.
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN ln -fs /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

COPY crawler/config.py /
COPY crawler/crawler.py /

CMD python3 crawler.py
