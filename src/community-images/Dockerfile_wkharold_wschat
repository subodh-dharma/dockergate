FROM golang:1.4.2

RUN go get github.com/gorilla/websocket

WORKDIR /go/src/github.com/gorilla/websocket/examples/chat
RUN go install ./...

ENTRYPOINT ["/go/bin/chat"]
