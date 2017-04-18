#!/bin/bash
apt-get -q update
apt-get install -y -q file
find / -print| while IFS='"'  read -r file
do 
    VAR=`file "$file"`
    echo $VAR
    case "$VAR" in *ELF*):
	echo "ELF ELF ELF"
	ldd "$file"
	echo "ELF END";
    esac
done
