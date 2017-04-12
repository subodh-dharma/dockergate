FROM golang:1.6
ADD . /go/src/github.com/jdassonvil/pkgserver
RUN go install github.com/jdassonvil/pkgserver

ENTRYPOINT /go/bin/pkgserver

EXPOSE 3535

RUN mkdir /resources
