#!/bin/bash
docker stop $(sudo docker ps -a -q)
docker rm $(sudo docker ps -a -q)
docker rmi $(sudo docker images -q)
#mkdir -p $(pwd)/final_output/$1
#cp -r $(pwd)/test_env/$1/output $PWD/final_output/$1
rm -rf $(pwd)/test_env/$1
exit
