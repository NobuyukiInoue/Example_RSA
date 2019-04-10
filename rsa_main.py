# -*- coding: utf-8 -*-

from my_modules import rsa

def main():

  """公開鍵と秘密鍵を生成"""
#  public_key, private_key = rsa.generate_keys(101, 3259)
  public_key, private_key = rsa.generate_keys(101, 3259)

  plain_text = "この文字列を暗号化／復号化するよ♪"

  print("秘密鍵:(E = %d, N = %d)" %(public_key[0], public_key[1]))
  print("公開鍵:(D = %d, N = %d)" %(private_key[0], private_key[1]))
  print("平文:%s" %plain_text)

  """暗号文を生成する"""
  encrypted_text = rsa.encrypt(plain_text, public_key)
  print("暗号文:%s" %rsa.sanitize(encrypted_text))

  """暗号文から平文を復元する"""
  decrypted_text = rsa.decrypt(encrypted_text, private_key)
  print("平文:%s" %decrypted_text)


if __name__ == "__main__":
  main()
