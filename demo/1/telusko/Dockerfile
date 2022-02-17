FROM python:3.8.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirments.txt /app/

RUN pip install -r requirments.txt

COPY . /app/

