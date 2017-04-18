#! /bin/bash
apt-get -q update
apt-get install -y -q file
apt-get install -y -q binutils

find / -print | while IFS='"'  read -r file
do 
    VAR=`file "$file"`
    #echo $VAR > /dev/null
    case "$VAR" in *ELF*):
        echo "ELF NM BEGIN FOR: $file"
        nm -D "$file"
        echo "ELF NM END FOR: $file"; 
    esac
done
