# -*- coding:utf-8 -*-

import base64
import os
import sys

def main():
    print("Please Input BASE64 Strings.")
    print("(Reading ends when you enter a blank line.)")

    lines = ""
    while True:
        line = input().rstrip()
        if len(line) > 0:
            lines += line
        else:
            break

    print("BASE64 Decoding Start...")
    # base64でencode
    dec_data = base64.b64decode( lines )

    # 16進数で出力
    print("key_size = %d byte (%d bit)" %(len(dec_data), len(dec_data)*8) )
    for data in dec_data:
        print("%02X" %data, end="")
    print(data)

    # decodeしてもとデータに変換
    enc_data = base64.b64encode( dec_data ).decode('sjis')

    if enc_data == lines:
        print("Verify Check ... Success.")
    else:
        print("Verify Check ... Failed.")


if __name__ == "__main__":
    main()
