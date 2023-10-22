FROM python:3.10-slim

ENV HOST=0.0.0.0
ENV PORT=80

WORKDIR /picobrew_pico

RUN apt-get update && \
    apt-get install -y bluez bluetooth git gcc g++ && \
    apt-get clean

RUN pip3 install -U pip

# Avoid cache purge by adding requirements first
COPY requirements.txt /picobrew_pico/requirements.txt
RUN pip install -r requirements.txt

COPY . /picobrew_pico

CMD python3 server.py ${HOST} ${PORT}
