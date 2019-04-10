# -*- coding: utf-8 -*-

from msvcrt import getch
import os
import sys

from my_modules import rsa


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s [encrypt | decrypt | create_key] cleartext_file [encrypted_file]" %(argv[0]))
        print("example1) -- create_key\n"
              "python rsa_main.py create_key\n\n"
              "example2) -- encrypt\n"
              "python rsa_main.py encrypt clearfile.txt encrypted.txt\n\n"
              "example3) -- decrypt\n"
              "python rsa_main.py decrypt encrypted.txt\n")
        exit(0)

    if argv[1] == "create_key":
        create_key()

    else:
        if argc < 3:           
            print("Usage: python %s [encrypt | decrypt | create_key] filename" %(argv[0]))
            exit(0)

        filename = argv[2]
        if not os.path.exists(filename):
            print("%s not found..." %filename)
            exit(0)

        if argv[1] == "encrypt":
            encrypt(filename)

        elif argv[1] == "decrypt":
            decrypt(filename)


def check_targetfile_exists(filename):
    if not os.path.exists(filename):
        print("%s not found..." %filename)
        exit(0)


def create_key():
    """公開鍵と秘密鍵を生成"""
    public_key, private_key = rsa.generate_keys(101, 3259)

    print("Public key filename [rsa_public.key]:", end = '')
    public_key_filename = input()
    if public_key_filename == "":
        public_key_filename = "rsa_public.key"

    print("Private key filename [rsa_private.key]:", end = '')
    private_key_filename = input()
    if private_key_filename == "":
        private_key_filename = "rsa_private.key"

    with open(public_key_filename, mode='w') as f:
        f.writelines("%d,%d" %(public_key[0], public_key[1]))

    with open(private_key_filename, mode='w') as f:
        f.writelines("%d,%d" %(private_key[0], private_key[1]))

    print("Create Keys done.")


def read_keys():
    public_key_filename  = "rsa_public.key"
    private_key_filename = "rsa_private.key"

    """公開鍵ファイルの読み込み"""
    f1 = open(public_key_filename, "r")
    lines = f1.readlines()

    """最初の１行から２つの値を読み込む"""
    flds = lines[0].split(",")
    public_key = (int(flds[0]), int(flds[1]))

    """秘密鍵ファイルの読み込み"""
    f2 = open(private_key_filename, "r")
    lines = f2.readlines()

    """最初の１行から２つの値を読み込む"""
    flds = lines[0].split(",")
    private_key = (int(flds[0]), int(flds[1]))

    return public_key, private_key


def encrypt(cleartext_fname):
    """鍵ファイルから公開鍵を読み込む"""
    public_key, _ = read_keys()

    """平文ファイルを読み込む"""
    f = open(cleartext_fname, "rt", encoding="utf-8")
    lines = f.readlines()

    plain_text = ""
    for line in lines:
        plain_text += line

    """暗号化および結果の出力"""
    encrypted_text = rsa.encrypt(plain_text, public_key)
#    print(rsa.sanitize(encrypted_text))
    print(encrypted_text)


def decrypt(filename):
    """鍵ファイルから秘密鍵を読み込む"""
    _, private_key = read_keys()

    """暗号文ファイルを読み込む"""
    f = open(filename, "r")
    lines = f.readlines()

    encrypted_text = ""
    for line in lines:
        encrypted_text += line

    """復号化および結果の出力"""
    decrypted_text = rsa.decrypt(encrypted_text, private_key)
    print(decrypted_text)


if __name__ == "__main__":
    main()
