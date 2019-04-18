#!/bin/bash

public_key=./rsa_public.key
private_key=./rsa_private.key
file1=./base64_work/image.jpg
file2=./test.bin
file3=./test.jpg

if [ -f $public_key ]; then
    rm $public_key
fi

if [ -f $private_key ]; then
    rm $private_key
fi

if [ -f $file2 ]; then
    rm $file2
fi

if [ -f $file3 ]; then
    rm $file3
fi

python ./rsa_main_mode_bin.py create_key
python ./rsa_main_mode_bin.py encrypt $file1 $file2 $public_key
python ./rsa_main_mode_bin.py decrypt $file2 $file3 $private_key

cat $public_key
echo -e -n "\n"

cat $private_key
echo -e -n "\n"

result1=`python ./print_FileHash.py $file1`
result2=`python ./print_FileHash.py $file3`

echo $file1":"$result1
echo $file3":"$result2

if [ "$result1" = "$result2" ]; then
    echo -n -e "\033[0;32m"
    echo -n "Success."
    echo -n -e "\033[0;39m"
else
    echo -n -e "\033[0;31m"
    echo -n "Failed."
    echo -n -e "\033[0;39m"
fi
