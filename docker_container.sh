#!/bin/bash
original_name=$1
filename=${original_name/\//_}
filename="${filename}.json"
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1 uname
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1 echo "hi"
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1 /bin/bash
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1 "mkdir -p /home/ubuntu/folder;ls"
echo "Done!"
