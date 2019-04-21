#!/bin/bash

cmd="./test_mode_bin.sh"
keyfile1="public.key"
keyfile2="private.key"
file1="./original.jpg"
file2="./test.bin"
file3="./test.jpg"


echo -e "\033[0;35m#### encrypt(public_key) --> decrypt(private_key) ###\033[0;39m"

for ((i=0; i < 10; i++)); do
    $cmd $keyfile1 $keyfile2 $file1 $file2 $file3
done


echo -e "\033[0;35m#### encrypt(private_key) --> decrypt(public_key) ###\033[0;39m"

for ((i=0; i < 10; i++)); do
    $cmd $keyfile1 $keyfile2 $file1 $file2 $file3 0
done
