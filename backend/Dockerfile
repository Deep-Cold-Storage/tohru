FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip

COPY requirements.txt /
RUN pip3 install -r requirements.txt

# Setup default time zone.
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN apt install tzdata
RUN ln -fs /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

COPY tohru/ /

CMD gunicorn -b 0.0.0.0:8000 tohru:app
