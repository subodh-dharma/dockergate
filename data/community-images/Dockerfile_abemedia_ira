FROM golang:1.6
MAINTAINER Adam Bouqdib <adam@abemedia.co.uk>

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

COPY . /go/src/app
RUN go-wrapper download
RUN go-wrapper install

EXPOSE 8080

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive && \
    apt-get -yq install mysql-client && \
    rm -rf /var/lib/apt/lists/*

CMD ["./run.sh"]
