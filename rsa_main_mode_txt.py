# -*- coding: utf-8 -*-

from my_modules.getch import getch
import os
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
        if argc < 4:           
            exit_msg(argv[0])

        filename = argv[2]
        if not os.path.exists(filename):
            print("%s not found." %filename)
            exit(0)
        
        keyfile = argv[3]
        if not os.path.exists(keyfile):
            print("%s not found." %keyfile)
            exit(0)

        if argc >= 5:
            char_code = argv[4]
        else:
            char_code = "utf-8"

        if argv[1] == "encrypt" or argv[1] == "enc":
            encrypt(keyfile, filename, char_code)
        elif argv[1] == "decrypt" or argv[1] == "dec":
            decrypt(keyfile, filename, char_code)
        else:
            exit_msg(argv[0])

def exit_msg(argv0):
    print("Usage: python %s [encrypt | decrypt | create_key] [平文ファイル | 暗号化ファイル] [公開鍵ファイル | 秘密鍵ファイル] [sjis | utf-8]" %argv0)
    print("example1) -- create_key\n"
            "python rsa_main_mode_txt.py create_key\n\n"
            "example2-1) -- encrypt(macOS/Linux)\n"
            "python rsa_main_mode_txt.py encrypt clearfile.txt rsa_public.key utf-8\n\n"
            "example2-2) -- decrypt(macOS/Linux)\n"
            "python rsa_main_mode_txt.py decrypt encrypted.txt rsa_private.key utf-8\n\n"
            "example3-1) -- encrypt(Windows)\n"
            "python rsa_main_mode_txt.py encrypt clearfile.txt rsa_public.key sjis\n\n"
            "example3-2) -- decrypt(Windows)\n"
            "python rsa_main_mode_txt.py decrypt encrypted.txt rsa_private.key sjis\n\n")
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
        print("%s is exists." %filename)
        print("overwrite ? (Y/N):", end=None)

        firstKey = ''
        while (firstKey != 'Y' and firstKey != 'N'):
            print("\n%s is exists. overwrite? (Y/N)" %filename, end = "")
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


def encrypt(keyfile, filename, char_code):
    """鍵ファイルから公開鍵を読み込む"""
    public_key = read_key(keyfile)

    """平文ファイルを読み込む"""
    f = open(filename, "rt", encoding=char_code)
    try:
        lines = f.readlines()
    except UnicodeDecodeError as e:
        print(e)
        print("%s の文字コードは %s ではないかもしれません。" %(filename, char_code))
        exit(0)

    plain_text = ""
    for line in lines:
        plain_text += line

    """暗号化および結果の出力"""
    encrypted_text = rsa.encrypt_from_text(plain_text, public_key)
    print(encrypted_text)


def decrypt(keyfile, filename, char_code):
    """鍵ファイルから秘密鍵を読み込む"""
    private_key = read_key(keyfile)

    """暗号文ファイルを読み込む"""
    f = open(filename, "r", encoding=char_code)
    try:
        lines = f.readlines()
    except UnicodeDecodeError as e:
        print(e)
        print("%s の文字コードは %s ではないかもしれません。" %(filename, char_code))
        exit(0)

    encrypted_text = ""
    for line in lines:
        encrypted_text += line

    """復号化および結果の出力"""
    decrypted_text = rsa.decrypt_to_text(encrypted_text.strip(), private_key)

    print(decrypted_text)


if __name__ == "__main__":
    main()
