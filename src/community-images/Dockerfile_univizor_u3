FROM python:3.5-alpine

MAINTAINER "Jozko Skrablin"

RUN apk add --no-cache -qq libffi gcc postgresql-dev musl-dev bash libffi-dev libffi-dev libxslt-dev zlib libjpeg-turbo-dev

RUN adduser -D -u 3000 u3

RUN mkdir -p /home/u3/tmp && \
  mkdir -p /home/u3/data/files

ADD . /home/u3

RUN chown -R u3:u3 /home/u3

ADD ./bin/run-scrapy.sh /usr/local/bin/run-scrapy.sh
RUN chmod +x /usr/local/bin/run-scrapy.sh

RUN pip install dumb-init && \
  pip install --upgrade -r /home/u3/requirements.txt

WORKDIR /home/u3

VOLUME ["/home/u3/data/files", "/home/u3/tmp"]

RUN chown -R u3:u3 /home/u3

ENV U3_USER="u3" \
  U3_HOME="/home/u3" \
  CONCURRENT_REQUESTS="8" \
  DOWNLOAD_DELAY="3" \
  FILES_STORE="/home/u3/data/files" \
  U3_ENV="production"

ENV HASHING_ALGORITHM sha256

USER u3

ENTRYPOINT ["/usr/local/bin/run-scrapy.sh"]
