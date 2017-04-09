#!/bin/bash

var=`docker images|grep $1|tr -s ' '|cut -d ' ' -f3`
echo $var
docker rmi $var
mkdir -p ~/OS_Sec/final_output/$1

cp -r ~/OS_Sec/test_env/$1/output ~/OS_Sec/final_output/$1
rm -rf ~OS_Sec/test_env/$1
