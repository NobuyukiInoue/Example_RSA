# -*- coding:utf-8 -*-

import base64
import os
import sys

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
        print("Usage: python %s image_file" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    #file読み込み
    file = open(argv[1], 'rb').read()

    #base64でencode
    enc_file = base64.b64encode( file )

    #encodeしたascii文字列を出力
    print(enc_file)

    #decodeしてもとデータに変換
    dec_file = base64.b64decode( enc_file )

    #decodeしたデータと元データを比較
    if file == dec_file :
        print('SAME')
    else :
        print('NOT SAME')

if __name__ == "__main__":
  main()
