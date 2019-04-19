#!/bin/bash

cmd="./repeated_test.sh"
keyfile1="key1.key"
keyfile2="key2.key"
file1="./image.jpg"
file2="./test.bin"
file3="./test.jpg"


echo -e "\033[0;31m#### encrypt(public_key) --> decrypt(private_key) ###\033[0;39m"

for ((i=0; i < 10; i++)); do
    $cmd $keyfile1 $keyfile2 $file1 $file2 $file3
done


echo -e "\033[0;31m#### encrypt(private_key) --> decrypt(public_key) ###\033[0;39m"

for ((i=0; i < 10; i++)); do
    $cmd $keyfile2 $keyfile1 $file1 $file2 $file3
done
