FROM python:3.8-alpine

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip3 install Flask


CMD [ "python3", "app.py"]