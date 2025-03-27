FROM python:3.12-slim-bullseye

RUN apt-get update && \
    apt-get install -y sudo && \
    adduser --disabled-password --gecos '' appuser && \
    adduser appuser sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .

USER appuser

CMD [ "python3", "main.py" ]