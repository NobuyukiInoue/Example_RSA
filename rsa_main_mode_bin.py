# -*- coding: utf-8 -*-

from my_modules.getch import getch
import os
import struct
import sys
from my_modules import rsa


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        exit_msg(argv[0])

    if argv[1] == "create_key" or argv[1] == "key":
        create_key()
    else:
        if argc < 5:           
            exit_msg(argv[0])

        r_file = argv[2]
        if not os.path.exists(r_file):
            print("%s not found." %r_file)
            exit(0)

        w_file = argv[3]
        check_exists(w_file)

        keyfile = argv[4]
        if not os.path.exists(keyfile):
            print("%s not found." %keyfile)
            exit(0)

        if argv[1] == "encrypt" or argv[1] == "enc":
            encrypt_binary(keyfile, r_file, w_file)
        elif argv[1] == "decrypt" or argv[1] == "dec":
            decrypt_binary(keyfile, r_file, w_file)
        else:
            exit_msg(argv[0])


def exit_msg(argv0):
    print("Usage: python %s [encrypt | decrypt | create_key] [変換前ファイル] [変換後ファイル] [公開鍵ファイル] | 秘密鍵ファイル]" %argv0)
    print("example1) -- create_key\n"
            "python rsa_main.py create_key\n\n"
            "example2) -- encrypt"
            "python rsa_main.py encrypt file1 file2 rsa_public.key\n\n"
            "example3) -- decrypt"
            "python rsa_main.py decrypt file2 file1 rsa_private.key\n\n")
    exit(0)


def create_key():
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
    p, q = rsa.calc_p_q(30, 3000)
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


def read_key(keyfilename):
    """鍵ファイルの読み込み"""
    f1 = open(keyfilename, "r")
    lines = f1.readlines()

    """最初の１行から２つの値を読み込む"""
    flds = lines[0].split(",")
    return (int(flds[0]), int(flds[1]))


def encrypt_binary(keyfile, read_file, write_file):
    """鍵ファイルから公開鍵を読み込む"""
    public_key = read_key(keyfile)

    """平文ファイルを読み込む"""
    f = open(read_file, "rb")
    plain_integers = []
    while True:
        d = f.read(1)
        if len(d) == 0:
            break
        plain_integers.append(int.from_bytes(d, byteorder='big'))
    f.close

    """暗号化および結果の出力"""
    encrypted_integers = rsa.encrypt_from_binary(plain_integers, public_key)
    with open(write_file, 'wb') as f:
        for d in encrypted_integers:
            f.write(d.to_bytes(8, byteorder='big'))


def decrypt_binary(keyfile, read_file, write_file):
    """鍵ファイルから秘密鍵を読み込む"""
    private_key = read_key(keyfile)

    """暗号文ファイルを読み込む"""
    f = open(read_file, "rb")
    encrypted_integers = []
    while True:
        d = f.read(8)
        if len(d) == 0:
            break
        encrypted_integers.append(int.from_bytes(d, byteorder='big'))
    f.close

    """復号化および結果の出力"""
    decrypted_integers = rsa.decrypt_to_binary(encrypted_integers, private_key)
    with open(write_file, 'wb') as f:
        for d in decrypted_integers:
            f.write(d.to_bytes(1, byteorder='big'))


if __name__ == "__main__":
    main()
