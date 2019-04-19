# Example_RSA
RSA暗号化方式を独自実装したプログラムです。

* テキストファイル専用の rsa_main_mode_txt.py
* バイナリモード（テキスト形式にも対応）の rsa_main_mode_bin.py

の２つのメインプログラムがあります。

どちらのプログラムも、

* 公開鍵で暗号化し、秘密鍵で復号化する（暗号化データの送受信）
* 秘密鍵で暗号化し、公開鍵で復号化する（電子署名の送付・確認）

ことができます。

そのほか、元ファイルと復元後のファイルの内容のチェック用に
ファイルのハッシュ値を出力するツールとして、

*ファイルのハッシュ値出力ツール print_FileHash.py

を用意しています。
<br>
<br>

## 1. テキストファイル専用(rsa_main_mode_txt.py)の使用方法

テキストファイル専用のrsa_main_mode_txt.py は、
テキスト形式(SJISまたはUTF-8)の平文にのみ対応しています。
<br>
暗号化後の結果は標準出力に出力します。
結果をファイルに保存したい場合はリダイレクトを利用します。
<br>
<br>

### 1-1. キーの生成（rsa_main_mode_txt.py）
公開鍵／秘密鍵を生成します。
生成された鍵は、デフォルトではそれぞれ"rsa_public.key", "rsa_private.key"というファイルに出力されます。
```
$ python rsa_main_mode_txt.py create_key
Public key filename [rsa_public.key]:
Private key filename [rsa_private.key]:
Create Keys done.
```
<br>
<br>

### 1-2. 平文ファイルから暗号化後の文字列を生成する（rsa_main_mode_txt.py）
"rsa_main_mode_txt.py encrypt"に続けて、平文ファイル、公開鍵ファイル 平文ファイルの文字コードを指定して
rsa_main_mode_txt.pyを実行します。
```
$ python rsa_main_mode_txt.py encrypt 平文ファイル 公開鍵ファイル utf-8
```
または
```
PS D:\> python rsa_main_mode_txt.py encrypt 平文ファイル 公開鍵ファイル sjis
```

なお、出力する文字列をファイルに保存したい場合は、以下のようにリダイレクトを利用すると良いでしょう。

```
$ python rsa_main_mode_txt.py encrypt 平文ファイル 公開鍵ファイル utf-8 > 出力ファイル名
```
または
```
PS D:\> python rsa_main_mode_txt.py encrypt 平文ファイル 公開鍵ファイル sjis > 出力ファイル名
```
MS-WindowsのPowerShellでリダイレクトを行った場合、デフォルトでは文字コードがUnicodeとして出力されるため、
必要に応じて出力後の結果をテキストエディタ等でsjisまたはutf-8に変換して再保存しておいてください。
<br>
<br>

### 1-3. 暗号化後の文字列を保存したファイルから平文の文字列を復号化する（rsa_main_mode_txt.py）
"rsa_main_mode_txt.py decrypt"に続けて、暗号化後の出力結果ファイル、秘密鍵ファイル、文字コードを指定して
rsa_main_mode_txt.pyを実行します。

```
$ python rsa_main_mode_txt.py decrypt 暗号化後の出力結果ファイル 秘密鍵ファイル utf-8
```
または
```
PS D:\> python rsa_main_mode_txt.py decrypt 暗号化後の出力結果ファイル 秘密鍵ファイル sjis
```
<br>
<br>

### 1-4. 暗号化と復号化の実行例（rsa_main_mode_txt.py）
```
$ cat file1.txt
暗号化の実験です。
読めますか？
$
$ python rsa_main_mode_txt.py encrypt file1.txt rsa_public.key utf-8
000141cd00028415000147af0004c5f40004f21100014b4c0003cb2f0001ddc00002c59c0001e92e0001dc890000d9220001bf590001ddc00001859300003ba40001e92e
$
$ python rsa_main_mode_txt.py encrypt file1.txt rsa_public.key utf-8 > file2.txt
$
$ python rsa_main_mode_txt.py decrypt file2.txt rsa_private.key utf-8
暗号化の実験です。
読めますか？
```
<br>
<br>

## 2. バイナリモード用(rsa_main_mode_bin.py)の使用方法

バイナリモード用のrsa_main_mode_txt.py は、
暗号化後の結果をファイルに出力します。
変換前のファイル名のほかに、変換後のファイル名も指定して実行します。
<br>
<br>

### 2-1. キーの生成（rsa_main_mode_bin.py）
公開鍵／秘密鍵を生成します。
生成された鍵は、デフォルトではそれぞれ"rsa_public.key", "rsa_private.key"というファイルに出力されます。
```
$ python rsa_main_mode_bin.py create_key
Public key filename [rsa_public.key]:
Private key filename [rsa_private.key]:
Create Keys done.
```
<br>
<br>

### 2-2. 元ファイルから暗号化ファイルを生成する（rsa_main_mode_bin.py）
"rsa_main_mode_bin.py encrypt"に続けて、暗号化したい元ファイル名、暗号化後のファイル名、公開鍵ファイルを指定して
rsa_main_mode_bin.pyを実行します。
```
$ python rsa_main_mode_bin.py encrypt 暗号化したい元ファイル名 暗号化後のファイル名 公開鍵ファイル
```
<br>
<br>

### 2-3. 暗号化後のファイルから元のファイルを復号化する（rsa_main_mode_bin.py）
"rsa_main_mode_bin.py decrypt"に続けて、暗号化後のファイル名、復元後のファイル名、秘密鍵ファイルを指定して
rsa_main_mode_bin.pyを実行します。

```
$ python rsa_main_mode_bin.py decrypt 暗号化後の出力結果ファイル 復元後のファイル名 秘密鍵ファイル
```
<br>
<br>

### 2-4. 暗号化と復号化の実行例（rsa_main_mode_bin.py）

暗号化処理例
```
$ python rsa_main_mode_bin.py encrypt image1.jpg testimage.bin rsa_public.key
```

復号化処理例
```
$ python rsa_main_mode_bin.py decrypt testimage.bin image2.jpg rsa_private.key
```
<br>
<br>

## 3. 検証用スクリプト

下記のサブディレクトリに、鍵の生成、暗号化、復号化処理および
元ファイルと復元後ファイルのハッシュ値比較を行うスクリプトを配置しています。

* ./TestScripts/ps1    ... PowerShell用スクリプト群
* ./TestScripts/bash   ... bash用スクリプト群

それぞれ、

* 鍵ペアの生成および公開鍵による暗号化および秘密鍵による復号化
* 鍵ペアの生成および秘密鍵による暗号化および公開鍵による復号化

を10回づつ実行します。
<br>
<br>

## 3-1. 検証用スクリプト実行方法(bash版)

```
$ cd TestScripts/bash
$ ./repeated_main.sh
#### encytpt(public_key) --> decrypte(private_key) ###
Public key filename [rsa_public.key]:Private key filename [rsa_private.key]:Create Keys done.
key2.key            :7,4562471
key1.key            :390703,4562471
python ../../rsa_main_mode_bin.py encrypt ./image.jpg ./test.bin ./key1.key
python ../../rsa_main_mode_bin.py decrypt ./test.bin ./test.jpg ./key2.key
./image.jpg         :SHA2 : 351efe5e4d33d7ca16c86b3137c78011
./test.jpg          :SHA2 : 351efe5e4d33d7ca16c86b3137c78011
<<Success>>
   ...
   ...
```
<br>
<br>

## 3-2. 検証用スクリプト実行方法(PowerShell版)

```
PS D:\work\Example_RSA> cd .\TestScripts\ps1
PS D:\work\Example_RSA\TestScripts\ps1>.\repeated_main.ps1

#### encytpt(public_key) --> decrypte(private_key) ###
repeated_test.ps1 ./key1.key ./key2.key ./image.jpg ./test.bin ./test.jpg
Public key filename [rsa_public.key]:Private key filename [rsa_private.key]:Create Keys done.
./key1.key           : 5,6107737
./key2.key           : 813701,6107737
python ../../rsa_main_mode_bin.py encrypt ./image.jpg ./test.bin ./key1.key
python ../../rsa_main_mode_bin.py decrypt ./test.bin ./test.jpg ./key2.key
./image.jpg          SHA2 : 351efe5e4d33d7ca16c86b3137c78011
./test.jpg           SHA2 : 351efe5e4d33d7ca16c86b3137c78011
<<Sucess>>
    ....
    ....
```
<br>
<br>
