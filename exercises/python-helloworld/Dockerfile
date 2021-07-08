# Base image for the container
FROM python:3.8

# set a key-value label for the Docker image
LABEL maintainer="Stephen Akuffo by way of Katie Gamanji"

COPY . /app

WORKDIR /app

# PIP install the requirements
RUN pip install -r requirements.txt

# start the app
CMD [ "python", "app.py" ]