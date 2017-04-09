#!/bin/bash

var=$PWD/test_env/$1
echo $var
mkdir -p $var
cp -r $PWD/src $var
cp -r $PWD/bin $var
cp -r $PWD/pkg $var
mkdir $var/output
export GOPATH=$var
export COLLECTOR_DIR=$GOPATH/src/github.com/banyanops/collector
export COLLECTOR_HOST_DIR=$var/output
export BANYAN_HOST_DIR=$var/output


$GOPATH/bin/collector registry-1.docker.io  $1 --maximages 1
