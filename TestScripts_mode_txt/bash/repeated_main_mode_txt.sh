#!/bin/bash

cmd="./test_mode_txt.sh"
keyfile1="public.key"
keyfile2="private.key"
file1="./original_utf8.txt"
file2="./test.bin"
file3="./test.txt"
mode="utf8"

echo -e "\033[0;35m#### encrypt(public_key) --> decrypt(private_key) ###\033[0;39m"

for ((i=0; i < 10; i++)); do
    $cmd $keyfile1 $keyfile2 $file1 $file2 $file3 $mode
done


echo -e "\033[0;35m#### encrypt(private_key) --> decrypt(public_key) ###\033[0;39m"

for ((i=0; i < 10; i++)); do
    $cmd $keyfile1 $keyfile2 $file1 $file2 $file3 $mode 0
done
