#!/bin/bash

export GOPATH=$(pwd)
export COLLECTOR_DIR=$GOPATH/src/github.com/banyanops/collector
export COLLECTOR_HOST_DIR=$(pwd)/output
export BANYAN_HOST_DIR=$(pwd)/output

cd $GOPATH

sudo apt-get install -y golang
go get -u github.com/banyanops/collector/...

cp run_nm.sh $COLLECTOR_DIR/data/userscripts
#cp print_file.sh $COLLECTOR_DIR/data/userscripts
#cp find_where.sh $COLLECTOR_DIR/data/userscripts
cp -r syscall_library/ $COLLECTOR_DIR/data/bin/

cd $COLLECTOR_DIR

export DOCKER_USER=$1
export DOCKER_PASSWORD=$2
#go test

#$GOPATH/bin/collector registry-1.docker.io  $1 --maximages 1
