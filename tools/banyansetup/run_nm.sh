#! /bin/bash
apt-get -q update
apt-get install -y -q file
apt-get install -y -q binutils

export SYSCALL="/banyancollector/bin"
ln -s $SYSCALL/python-static /bin/python 2>&1
cp -r $SYSCALL/syscall_library .
find / -print | while IFS='"'  read -r file
do 
    VAR=`file "$file"`
    #echo $VAR > /dev/null
    case "$VAR" in *ELF*executable*):
        echo "ELF NM BEGIN FOR: $file"
		cd syscall_library
		python check_index.py "$file" 2>&1
        nm -D "$file"
		cd -
        echo "ELF NM END FOR: $file"; 
    esac
done
cd syscall_library
echo 'START INDEX'
cat index
echo 'END INDEX'
echo 'START JSON'
cat output_mapping
