# registry.namely.tech/namely/broadway-dev:v5
# If you change this file, or any of the dependencies, build a new image and
# increase the version number.
FROM golang:1.7
RUN apt-get update && \
    apt-get install --assume-yes git build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN go get github.com/tools/godep github.com/kisielk/errcheck github.com/golang/lint/golint

RUN mkdir -p /go/src/github.com/namely/broadway
WORKDIR /go/src/github.com/namely/broadway
