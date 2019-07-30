FROM ubuntu:latest
LABEL Description="Tohru - Backend"

RUN apt update && apt install -y python3 python3-pip gunicorn3
RUN pip3 install flask redis

# Changes time zone inside container.
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN apt install tzdata
RUN ln -fs /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

COPY app/config.py /
COPY app/app.py /

CMD gunicorn3 -b 0.0.0.0:8000 app:app
