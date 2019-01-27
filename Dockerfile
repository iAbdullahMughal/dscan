FROM ubuntu:16.04

MAINTAINER Muhammad Abdullah "iamabdullahmughal@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev p7zip-full libfuzzy-dev libpulse-dev libffi-dev g++ libssl-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]