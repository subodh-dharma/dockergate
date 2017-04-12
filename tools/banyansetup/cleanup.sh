#!/bin/bash

#var=`docker images|grep $1|tr -s ' '|cut -d ' ' -f3`
#echo $var
docker rmi $1
mkdir -p $PWD/final_output/$1

cp -r $PWD/test_env/$1/output $PWD/final_output/$1
rm -rf $PWD/test_env/$1
