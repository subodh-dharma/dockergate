#!/bin/bash

python dockergate.py $1;
original_name=$1
filename=${original_name/\//_}
filename="${filename}.json"
cat data/policy/$filename | grep -o "SCMP_ACT_ALLOW" | wc -l
echo $filename
cmnd='docker run -d -it --security-opt=seccomp=data/policy/'${filename}
cmnd="${cmnd} "${original_name}
sudo tools/systemtap/syscall_chk.stp -c  "$cmnd" | wc -l
