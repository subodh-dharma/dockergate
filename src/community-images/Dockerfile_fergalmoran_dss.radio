FROM ubuntu:latest
MAINTAINER Fergal Moran <Ferg@lMoran.me>

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y python-setuptools python-pip git pkg-config libshout3 libshout3-dev python-dev

RUN mkdir /code/
WORKDIR /code

ADD requirements.txt /code/
ADD server.py /code/
ADD start.sh /code/
ADD ice_relay.py /code/
ADD static /code/static/
ADD util /code/util/
ADD templates /code/templates/

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["./start.sh"]
