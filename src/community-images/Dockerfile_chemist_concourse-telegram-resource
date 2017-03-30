FROM alpine:edge
MAINTAINER Alexey Smirnov <chemistmail@gmail.com>

RUN apk update && apk upgrade && \
    apk add --update  bash jq curl

COPY ./assets/* /opt/resource/
