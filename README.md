# Example_RSA
RSA暗号化方式を独自実装したプログラムです。

##キーの生成
```
python rsa_main.py create_key
```

##平文ファイルから暗号化後の文字列を生成する

```
python rsa_main.py encrypt clearfile.txt rsa_public.key utf-8
```
または
```
python rsa_main.py encrypt clearfile.txt rsa_public.key sjis
```


なお、出力する文字列をファイルに保存したい場合は、以下のようにリダイレクトを利用すると良いでしょう。

```
python rsa_main.py encrypt clearfile.txt rsa_public.key utf-8 > 出力ファイル名
```
または
```
python rsa_main.py encrypt clearfile.txt rsa_public.key sjis > 出力ファイル名
```
MS-WindowsのPowerShellでリダイレクトを行った場合、デフォルトでは文字コードがUnicodeとして出力されるため、
必要に応じて出力後の結果をテキストエディタ等でsjisまたはutf-8に変換して再保存しておいてください。
Unicode

##暗号化後の文字列を保存したファイルから平文の文字列を復号化する
```
python rsa_main.py decrypt encrypted.txt rsa_private.key utf-8
```
または
```
python rsa_main.py decrypt encrypted.txt rsa_private.key sjis
```
