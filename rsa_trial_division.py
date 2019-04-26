# -*- coding: utf-8 -*-

from my_modules.getch import getch
import math
import os
import struct
import sys
from my_modules import rsa


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        exit_msg(argv[0])

    if argv[1].isnumeric() == False:
        print("%s is not numeric." %argv[1])
        exit(1)

    N = int(argv[1])
    if N <= 0:
        print("%s is not positive integer." %argv[1])
        exit(1)
    
    for i in range(1, 512 + 1):
        if N <= pow(2, i):
            break
    print("%d <= pow(2, %d)" %(N, i))

    p_q = trial_division(N)
    print(p_q)

    if len(p_q) != 2:
        """素因数分解の結果が2個よりも多い場合は終了する"""
        exit(1)

    """鍵ペアを生成するかの確認処理"""
    firstKey = ''
    while (firstKey != 'Y' and firstKey != 'N'):
        print("\nDo you want to create a key? (Y/N):", end = "")
        keyRet = ord(getch())
        firstKey = chr(keyRet).upper()

    print()
    if (firstKey == 'N'):
        print("quit....")
        exit(0)

    """見つかった p, q から鍵ペアを生成する"""
    create_key_from_p_q(p_q[0], p_q[1])


def exit_msg(argv0):
    print("Usage: python %s value_N" %argv0)
    exit(0)


def create_key_from_p_q(p, q):
    print("Public key filename [rsa_public.key]:", end = '')
    public_key_filename = input()
    if public_key_filename == "":
        public_key_filename = "rsa_public.key"

    check_exists(public_key_filename)

    print("Private key filename [rsa_private.key]:", end = '')
    private_key_filename = input()
    if private_key_filename == "":
        private_key_filename = "rsa_private.key"

    check_exists(private_key_filename)

    """公開鍵と秘密鍵を生成"""
    # 30番目の素数以上、3000以下の素数からp, q を選ぶ
    public_key, private_key = rsa.generate_keys(p, q)

    with open(public_key_filename, mode='w') as f:
        f.writelines("%d,%d" %(public_key[0], public_key[1]))

    with open(private_key_filename, mode='w') as f:
        f.writelines("%d,%d" %(private_key[0], private_key[1]))

    print("Create Keys done.")


def check_exists(filename):
    if os.path.exists(filename):
        firstKey = ''
        while (firstKey != 'Y' and firstKey != 'N'):
            print("\n%s is exists. overwrite? (Y/N):" %filename, end = "")
            keyRet = ord(getch())
            firstKey = chr(keyRet).upper()

        print()
        if (firstKey == 'N'):
            print("quit....")
            exit(0)


def trial_division(n):
    """Return a list of the prime factors for a natural number."""

    """素因数を格納するリスト"""
    prime_list = []

    """2 ～ math.sqrt(n) の数字で割っていく"""
    tmp = int(math.sqrt(n)) + 1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            prime_list.append(num)

    """リストが空ならそれは素数"""
    if not prime_list:
        return 'prime number'
    else:
        prime_list.append(n)
        return prime_list

if __name__ == "__main__":
    main()
