#!/bin/bash
original_name=$1
filename=${original_name/\//_}
filename="${filename}.json"
echo ${filename}
cmnd="docker run -d -it --security-opt=seccomp=data/policy/${filename} ${1}"
echo "${cmnd}"
#sudo tools/systemtap/syscall_chk.stp -c  "$cmnd" | wc -l
docker pull $1
docker pull $1:release
docker run -d -it $1
docker ps -a > "tmp_status"
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1 uname
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1 echo "hi"
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1 /bin/bash 
docker run -d -it --security-opt=seccomp=data/policy/${filename} $1 "mkdir -p /home/ubuntu/folder;ls"

docker ps -a >> "tmp_status"
cat data/policy/${filename} | grep -o SCMP_ACT_ALLOW | wc -l >> "tmp_status"

docker stop $(sudo docker ps -a -q)
docker rm $(sudo docker ps -a -q)
docker rmi $(sudo docker images -q)
echo "Done!"
