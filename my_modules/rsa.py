# -*- coding: utf-8 -*-

import base64
import math
import random


def calc_p_q(primeNumber_indexMin, primeNumber_Max):
    """２つの素数(p, q)を求める"""

    """primeNumber_Max以下の素数のリストを取得する"""
    prime_list = sieve_of_eratosthenes(primeNumber_Max)

    """p*qの下限値をセット"""
    lower = math.pow(2, 16)

    while True:
        """primeNumber_indexMin以上、(len(prime_list) - 1)以下の数値の乱数を生成する"""
        x = random.randrange(primeNumber_indexMin, len(prime_list) - 1, 1)
        while True:
            """primeNumber_indexMin以上、(len(prime_list) - 1)以下の数値の乱数を生成する"""
            y = random.randrange(primeNumber_indexMin, len(prime_list) - 1, 1)
            if y != x:
                break
        if x * y > lower:
            break
 
    """得られた２つの素数を返す"""
    return prime_list[x], prime_list[y]


def sieve_of_eratosthenes(primeNumber_Max):
    """エラトステネスのふるいを利用して素数の配列を生成する"""

    dest = int(math.sqrt(primeNumber_Max))
    target_list = list(range(2, primeNumber_Max + 1))
    prime_list = []
 
    while True:
        num_min = min(target_list)
        if num_min >= dest:
            prime_list.extend(target_list)
            break
        prime_list.append(num_min)
 
        i = 0
        while True:
            if i >= len(target_list):
                break
            elif target_list[i] % num_min == 0:
                target_list.pop(i)
            i += 1

    return prime_list

def lcm(p, q):
    """
    最小公倍数を求める。
    """
    return (p * q) // math.gcd(p, q)


def generate_keys(p, q):
    """
    与えられた 2 つの素数 p, q から秘密鍵と公開鍵を生成する。
    """

    """２つの素数(p, q)の積nを求める"""
    N = p * q

    """p - 1 と q - 1 の最小公倍数を求める"""
    L = lcm(p - 1, q - 1)

    """公開鍵で使用するeを算出する"""
    for i in range(2, L):
        if math.gcd(i, L) == 1:
            E = i
            break

    """秘密鍵で使用するdを算出する"""
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


def encrypt_from_text(plain_text, public_key):
    """
    公開鍵 public_key を使って平文 plain_text を暗号化する。
    """
    E, N = public_key

    """平文文字列を数値に変換する"""
    plain_integers = [ord(char) for char in plain_text]

    """公開鍵（eと２つの素数の積n）を使って暗号化後の数値を生成する"""
    encrypted_integers = [pow(i, E, N) for i in plain_integers]

    """生成した数値を16進数文字列として出力する"""
    encrypted_text = ''.join(format(i, "08x") for i in encrypted_integers)

    return encrypted_text


def decrypt_to_text(encrypted_text, private_key):
    """
    秘密鍵 private_key を使って暗号文 encrypted_text を復号化する。
    """
    D, N = private_key
    
    encrypted_integers = []
    for i in range(0, len(encrypted_text), 8):
        """16進数として8文字づつ取り出し、整数に変換する"""
        encrypted_integers.append(int(encrypted_text[i:i+8], 16))

    """秘密鍵（dと２つの素数の積n）を使って、復号後の数値を求める"""
    decrypted_integers = [pow(i, D, N) for i in encrypted_integers]

    """復号後の数値を文字に変換し、連結する"""
    decrypted_text = ''.join(chr(i) for i in decrypted_integers)

    return decrypted_text


def encrypt_from_binary(plain_integers, public_key):
    """
    公開鍵 public_key を使って平文 plain_text を暗号化する。
    """
    E, N = public_key

    """公開鍵（eと２つの素数の積n）を使って暗号化後の数値を生成する"""
    return [pow(i, E, N) for i in plain_integers]


def decrypt_to_binary(encrypted_integers, private_key):
    """
    秘密鍵 private_key を使って暗号文 encrypted_text を復号化する。
    """
    D, N = private_key
    
    """秘密鍵（dと２つの素数の積n）を使って、復号後の数値を求める"""
    return [pow(i, D, N) for i in encrypted_integers]


def sanitize(encrypted_text):
    """
    UnicodeEncodeErrorを回避する。
    """
    return encrypted_text.encode('utf-8', 'replace').decode('utf-8')
