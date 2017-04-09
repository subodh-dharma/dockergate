FROM golang:1.8

# Install vendoring tools
RUN go get -u github.com/Masterminds/glide
RUN go get -u github.com/golang/dep
RUN go get -u github.com/kardianos/govendor
RUN go get -u github.com/tools/godep

# Install static analysis tools
RUN go get -u github.com/golang/lint/golint
RUN go get -u github.com/bradleyfalzon/apicompat/...
RUN go get -u honnef.co/go/tools/cmd/gosimple
RUN go get -u honnef.co/go/tools/cmd/staticcheck
RUN go get -u honnef.co/go/tools/cmd/unused

# Program to detect if file is generated or not
RUN go get -u github.com/gopherci/isFileGenerated

# Script to detect vendor tool and install deps
COPY install-deps.sh /usr/local/bin/

# Remove source code so we can clone into these directories if we happen
# to have fetched the tool and then receive a PR for it (we can't clone
# into a non-empty directory.)
RUN rm -rf $GOPATH/src/*

CMD ["sleep", "infinity"]
