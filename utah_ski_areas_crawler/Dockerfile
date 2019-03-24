# Use an official Python runtime as a parent image
FROM python:3.6-alpine

# Set the working directory to /crawler
WORKDIR /crawler

# Copy the current directory contents into the container at /crawler
COPY . /crawler

RUN apk add build-base

RUN apk add --no-cache bash

RUN apk add postgresql-dev

RUN pip3 install -r requirements.txt

CMD ["python3", "gather_snow_stats.py"]