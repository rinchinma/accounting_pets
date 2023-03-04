FROM python:3.8-slim-buster as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt

FROM python:3.8-slim-buster

RUN mkdir -p /accounting_pets

WORKDIR /accounting_pets

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p vol/web/media && mkdir -p vol/web/static

