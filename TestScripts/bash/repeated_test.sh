#!/bin/bash

##--------------------------------------------------------##
## �����`�F�b�N
##--------------------------------------------------------##

if [ $# -lt 5 ]; then
    printf "Usage) ${0} keyfile1 keyfile2 org_file encrypted_file decrypted_file"
    exit
fi

keyfile1=${1}
keyfile2=${2}
file1=${3}
file2=${4}
file3=${5}

if [ $# -ge 6 ]; then
    mode=${6}
else
    mode=1
fi

##--------------------------------------------------------##
## ���ؑΏۃv���O�����̎w��
##--------------------------------------------------------##

cmd_rsa_main="../../rsa_main_mode_bin.py"
cmd_filehash="../../print_FileHash.py"


##--------------------------------------------------------##
## �Ώۃt�@�C���̎��O�폜
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
## ���J���^�閧���t�@�C���̐���
##--------------------------------------------------------##

if [ $mode -eq 1 ]; then
    python $cmd_rsa_main create_key <<EOS
$keyfile1
$keyfile2
EOS

else
    python $cmd_rsa_main create_key <<EOS
$keyfile2
$keyfile1
EOS

fi


##--------------------------------------------------------##
## ���t�@�C���̓��e��\��
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
## �Í�������
##--------------------------------------------------------##

printf "python $cmd_rsa_main encrypt $file1 $file2 $keyfile1\n"
python $cmd_rsa_main encrypt $file1 $file2 $keyfile1


##--------------------------------------------------------##
## ����������
##--------------------------------------------------------##

printf "python $cmd_rsa_main decrypt $file2 $file3 $keyfile2\n"
python $cmd_rsa_main decrypt $file2 $file3 $keyfile2


##--------------------------------------------------------##
## �ϊ��O�t�@�C���ƕϊ���t�@�C���̃n�b�V���l���o�͂���
##--------------------------------------------------------##

result1=`python $cmd_filehash $file1`
result3=`python $cmd_filehash $file3`

printf "\033[0;36m"
printf "%-20s:" $file1
printf "$result1\n"
printf "%-20s:" $file3
printf "$result3\n"
printf "\033[0;39m"


##--------------------------------------------------------##
## ��v�^�s��v�̌��ʂ�\��
##--------------------------------------------------------##

if [ "$result1" = "$result3" ]; then
    printf "\033[0;32m<<Success>>\033[0;39m\n"
else
    printf "\033[0;31m<<Failed>>\033[0;39m\n"
fi
