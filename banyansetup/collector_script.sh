#!/bin/bash

var=~/OS_Sec/test_env/$1
echo $var
mkdir -p $var
cp -r ~/OS_Sec/src $var
cp -r ~/OS_Sec/bin $var
cp -r ~/OS_Sec/pkg $var
mkdir $var/output
export GOPATH=$var
export COLLECTOR_DIR=$GOPATH/src/github.com/banyanops/collector
export COLLECTOR_HOST_DIR=$var/output
export BANYAN_HOST_DIR=$var/output


$GOPATH/bin/collector registry-1.docker.io  $1 --maximages 1
