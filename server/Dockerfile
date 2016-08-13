FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update
# RUN apt-get install -y openssl libffi-dev libssl-dev libxml2-dev libxmlsec1-dev libldap2-dev
RUN apt-get install -y libpq-dev postgresql-client-9.4

WORKDIR /project/server

COPY pip.txt .
RUN pip install -r pip.txt

COPY . .
