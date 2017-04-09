
#!/bin/bash

export GOPATH=$PWD
export COLLECTOR_DIR=$GOPATH/src/github.com/banyanops/collector
export COLLECTOR_HOST_DIR=$PWD/output
export BANYAN_HOST_DIR=$PWD/output

sudo apt-get install -y golang
go get -u github.com/banyanops/collector/...

cd $COLLECTOR_DIR

export DOCKER_USER=$1
export DOCKER_PASSWORD=$2
go test

#$GOPATH/bin/collector registry-1.docker.io  $1 --maximages 1
