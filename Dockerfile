FROM docker.io/python:3.11-slim

USER root

RUN apt-get -y update
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN pip install flask

RUN mkdir /app
ENV AP /app
RUN mkdir $AP/volumes
RUN mkdir $AP/templates
RUN mkdir $AP/static

COPY ./server.py $AP/
COPY ./src/* $AP/

WORKDIR $AP

CMD ["sh", "-c", "python3 server.py"]
