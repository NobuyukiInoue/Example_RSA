#!/bin/bash

##--------------------------------------------------------##
## 引数チェック
##--------------------------------------------------------##

printf "args = ${0} ${1} ${2} ${3} ${4} ${5} ${6} ${7}\n"

if [ $# -lt 5 ]; then
    printf "Usage) ${0} keyfile1 keyfile2 org_file encrypted_file decrypted_file [code] [mode]\n"
    exit
fi

keyfile1=${1}
keyfile2=${2}
file1=${3}
file2=${4}
file3=${5}

if [ $# -ge 6 ]; then
    code=${6}
else
    code="utf8"
fi

if [ $# -ge 7 ]; then
    mode=${7}
else
    mode=1
fi


##--------------------------------------------------------##
## 検証対象プログラムの指定
##--------------------------------------------------------##

cmd_rsa_main="../../rsa_main_mode_txt.py"
cmd_filehash="../../print_FileHash.py"


##--------------------------------------------------------##
## 対象ファイルの事前削除
##--------------------------------------------------------##

if [ -f $keyfile1 ]; then
    rm $keyfile1
fi

if [ -f $keyfile2 ]; then
    rm $keyfile2
fi

if [ -f $file2 ]; then
    rm $file2
fi

if [ -f $file3 ]; then
    rm $file3
fi


##--------------------------------------------------------##
## 公開鍵／秘密鍵ファイルの生成
##--------------------------------------------------------##

printf "Execute: python $cmd_rsa_main create_key\n"

python $cmd_rsa_main create_key 1> /dev/null << EOS
$keyfile1
$keyfile2
EOS


##--------------------------------------------------------##
## 暗号化処理
##--------------------------------------------------------##

if [ $mode -eq 1 ]; then
    ## 公開鍵で暗号化
    printf "Execute: python $cmd_rsa_main encrypt $file1 $keyfile1 > $file2\n"
    python $cmd_rsa_main encrypt $file1 $keyfile1 > $file2
else
    ## 秘密鍵で暗号化
    printf "Execute: python $cmd_rsa_main encrypt $file1 $keyfile2 > $file2\n"
    python $cmd_rsa_main encrypt $file1 $keyfile2 > $file2
fi

##--------------------------------------------------------##
## 復号処理
##--------------------------------------------------------##

if [ $mode -eq 1 ]; then
    ## 秘密鍵で復号
    printf "Execute: python $cmd_rsa_main decrypt $file2 $keyfile2 > $file3\n"
    python $cmd_rsa_main decrypt $file2 $keyfile2 > $file3
else
    ## 公開鍵で復号
    printf "Execute: python $cmd_rsa_main decrypt $file2 $keyfile1 > $file3\n"
    python $cmd_rsa_main decrypt $file2 $keyfile1 > $file3
fi

##--------------------------------------------------------##
## 鍵ファイルの内容を表示
##--------------------------------------------------------##

key_result1=`cat $keyfile1`
key_result2=`cat $keyfile2`
printf "\033[0;33m"
printf "%-20s:" $keyfile1
printf "$key_result1\n"
printf "%-20s:" $keyfile2
printf "$key_result2\n"
printf "\033[0;39m"


##--------------------------------------------------------##
## 暗号化前ファイルと復号後ファイルを出力する
##--------------------------------------------------------##

printf "\033[0;36m###### 暗号化前:$file1 ######\033[0;39m\n"
cat $file1

printf "\033[0;36m###### 復号後:  $file3 ######\033[0;39m\n"
cat $file3

printf "\033[0;36m##################################\033[0;39m\n"
