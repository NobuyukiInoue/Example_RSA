# -*- coding: utf-8 -*-

from my_modules import rsa


def main():
    """公開鍵と秘密鍵を生成"""
#OK    public_key, private_key = rsa.generate_keys(101, 3259)
#OK    public_key, private_key = rsa.generate_keys(139, 2137)
#OK    public_key, private_key = rsa.generate_keys(373, 2137)
#OK    public_key, private_key = rsa.generate_keys(139, 2137)
#NG    public_key, private_key = rsa.generate_keys(3559, 2137)
#OK    public_key, private_key = rsa.generate_keys(139, 2137)
    # 30番目の素数以上、3000以下の素数からp, q を選ぶ
    p, q = rsa.calc_p_q(30, 3000)
    public_key, private_key = rsa.generate_keys(p, q)

    plain_text = "この文字列を暗号化／復号化するよ♪"

    print("秘密鍵:(E = %d, N = %d)" %(public_key[0], public_key[1]))
    print("公開鍵:(D = %d, N = %d)" %(private_key[0], private_key[1]))
    print("平文:%s" %plain_text)

    """暗号文を生成する"""
    encrypted_text = rsa.encrypt_from_text(plain_text, public_key)
    print("暗号文:%s" %rsa.sanitize(encrypted_text))

    """暗号文から平文を復元する"""
    decrypted_text = rsa.decrypt_to_text(encrypted_text, private_key)
    print("平文:%s" %decrypted_text)

    if plain_text == decrypted_text:
        print("p = %d, q = %d, Success." %(p, q))
    else:
        print("p = %d, q = %d, Fail." %(p, q))

if __name__ == "__main__":
    main()
