FROM bitnami/spark:3.5.0

USER root

RUN apt-get update && \
    apt-get install -y python3.11 python3.11-dev python3.11-venv && \
    ln -sf python3.11 /usr/bin/python3 && \
    ln -sf python3.11 /usr/bin/python

RUN apt-get install -y python3-pip && \
    python3.11 -m pip install --upgrade pip
