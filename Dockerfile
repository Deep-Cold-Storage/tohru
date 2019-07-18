FROM ubuntu:latest
LABEL Description="Tohru - Parser"

RUN apt update && apt install -y python3 python3-pip
RUN pip3 install openpyxl requests redis

# Changes time zone inside container.
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN apt install tzdata
RUN ln -fs /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

COPY parser/config.py /
COPY parser/parser.py /

CMD python3 parser.py
