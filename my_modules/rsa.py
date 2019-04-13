# -*- coding: utf-8 -*-

import base64
from math import gcd

def lcm(p, q):
    """
    最小公倍数を求める。
    """
    return (p * q) // gcd(p, q)


def generate_keys(p, q):
    """
    与えられた 2 つの素数 p, q から秘密鍵と公開鍵を生成する。
    """
    N = p * q
    L = lcm(p - 1, q - 1)

    for i in range(2, L):
        if gcd(i, L) == 1:
            E = i
            break

    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break
    """
    i = 0
    while True:
        if (i * L + 1) % E == 0:
            D = (i * L + 1) // E
            break
        i += 1
    """

    return (E, N), (D, N)


'''
def encrypt_org(plain_text, public_key):
    """
    公開鍵 public_key を使って平文 plain_text を暗号化する。
    """
    E, N = public_key
    plain_integers = [ord(char) for char in plain_text]
    encrypted_integers = [pow(i, E, N) for i in plain_integers]
    encrypted_text = ''.join(chr(i) for i in encrypted_integers)

    return encrypted_text
'''
def encrypt(plain_text, public_key):
    """
    公開鍵 public_key を使って平文 plain_text を暗号化する。
    """
    E, N = public_key

    # 平文文字列を数値に変換する
    plain_integers = [ord(char) for char in plain_text]

    # 公開鍵の２つの素数を使って暗号化後の数値を生成する
    encrypted_integers = [pow(i, E, N) for i in plain_integers]

    # 生成した数値を16進数文字列として出力する
    encrypted_text = ''.join(format(i, "08x") for i in encrypted_integers)

    return encrypted_text


'''
def decrypt_org(encrypted_text, private_key):
    """
    秘密鍵 private_key を使って暗号文 encrypted_text を復号化する。
    """
    D, N = private_key
    encrypted_integers = [ord(char) for char in encrypted_text]
    decrypted_intergers = [pow(i, D, N) for i in encrypted_integers]
    decrypted_text = ''.join(chr(i) for i in decrypted_intergers)

    return decrypted_text
'''
def decrypt(encrypted_text, private_key):
    """
    秘密鍵 private_key を使って暗号文 encrypted_text を復号化する。
    """
    D, N = private_key
    
    encrypted_integers = []
    for i in range(0, len(encrypted_text), 8):
        # 16進数として8文字づつ取り出し、整数に変換する
        encrypted_integers.append(int(encrypted_text[i:i+8], 16))

    # 秘密鍵の２つの素数を使って、復号後の数値を求める
    decrypted_intergers = [pow(i, D, N) for i in encrypted_integers]

    # 復号後の数値を文字に変換し、連結する
    decrypted_text = ''.join(chr(i) for i in decrypted_intergers)

    return decrypted_text


def sanitize(encrypted_text):
    """
    UnicodeEncodeError が置きないようにする。
    """
    return encrypted_text.encode('utf-8', 'replace').decode('utf-8')
