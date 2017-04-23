#!/bin/bash

docker rmi $1
mkdir -p $(pwd)/final_output/$1
cp -r $(pwd)/test_env/$1/output $PWD/final_output/$1
rm -rf $(pwd)/test_env/$1
