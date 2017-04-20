#!/bin/bash

#var=$(pwd)/test_env/$1
export BANYAN_ORIGIN=$(pwd)/tools/banyansetup
export GOPATH=$(pwd)/test_env/$1

echo $GOPATH

if [ -d "$GOPATH" ]; then
 rm -rf "$GOPATH"
fi

mkdir -p $GOPATH

cp -r $BANYAN_ORIGIN/src $GOPATH
cp -r $BANYAN_ORIGIN/bin $GOPATH
cp -r $BANYAN_ORIGIN/pkg $GOPATH
mkdir $GOPATH/output
#export GOPATH=$var
export COLLECTOR_DIR=$GOPATH/src/github.com/banyanops/collector
export COLLECTOR_HOST_DIR=$GOPATH/output
export BANYAN_HOST_DIR=$GOPATH/output
export BANYAN_OUTPUT_DIR=$GOPATH/output/hostcollector/banyanout


$GOPATH/bin/collector registry-1.docker.io  $1 --maximages 1
