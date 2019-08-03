FROM ubuntu:latest

RUN apt-get update && apt-get install -y locales libxml2-dev libxslt1-dev curl libsasl2-dev python-dev libldap2-dev libssl-dev && locale-gen ru_RU.UTF-8 && apt-get update && apt-get install -y python3-pip

ENV LANG=ru_RU.UTF-8 LC_ALL=ru_RU.UTF-8 LC_LANG=ru_RU.UTF-8

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD "./startup.sh"
