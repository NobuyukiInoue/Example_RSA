# Example_RSA
RSA暗号化方式を独自実装したプログラムです。
<br>
<br>

## キーの生成
公開鍵／秘密鍵を生成します。
生成された鍵は、デフォルトではそれぞれ"rsa_public.key", "rsa_private.key"というファイルに出力されます。
```
python rsa_main.py create_key
Public key filename [rsa_public.key]:
Private key filename [rsa_private.key]:
Create Keys done.
```
<br>
<br>

## 平文ファイルから暗号化後の文字列を生成する
"rsa_main.py encrypt"に続けて、平文ファイル、公開鍵ファイル 平文ファイルの文字コードを指定して
rsa_main.pyを実行します。
```
python rsa_main.py encrypt 平文ファイル 公開鍵ファイル utf-8
```
または
```
python rsa_main.py encrypt 平文ファイル 公開鍵ファイル sjis
```


なお、出力する文字列をファイルに保存したい場合は、以下のようにリダイレクトを利用すると良いでしょう。

```
python rsa_main.py encrypt 平文ファイル 公開鍵ファイル utf-8 > 出力ファイル名
```
または
```
python rsa_main.py encrypt 平文ファイル 公開鍵ファイル sjis > 出力ファイル名
```
MS-WindowsのPowerShellでリダイレクトを行った場合、デフォルトでは文字コードがUnicodeとして出力されるため、
必要に応じて出力後の結果をテキストエディタ等でsjisまたはutf-8に変換して再保存しておいてください。
<br>
<br>

## 暗号化後の文字列を保存したファイルから平文の文字列を復号化する
"rsa_main.py decrypt"に続けて、暗号化後の出力結果ファイル、秘密鍵ファイル、文字コードを指定して
rsa_main.pyを実行します。

```
python rsa_main.py decrypt 暗号化後の出力結果ファイル 秘密鍵ファイル utf-8
```
または
```
python rsa_main.py decrypt 暗号化後の出力結果ファイル 秘密鍵ファイル sjis
```
<br>
<br>

## 暗号化と復号化の実行例
```
$ cat 平文ファイル.txt
暗号化の実験です。
読めますか？
$ python rsa_main.py encrypt 平文ファイル.txt rsa_public.key utf-8
000141cd00028415000147af0004c5f40004f21100014b4c0003cb2f0001ddc00002c59c0001e92e0001dc890000d9220001bf590001ddc00001859300003ba40001e92e
$ python rsa_main.py encrypt 平文ファイル.txt rsa_public.key utf-8 > 暗号化後のファイル.txt
$ python rsa_main.py decrypt 暗号化後のファイル.txt rsa_private.key sjis
暗号化の実験です。
読めますか？
```
