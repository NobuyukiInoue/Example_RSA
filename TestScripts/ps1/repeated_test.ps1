param($keyfile1, $keyfile2, $file1, $file2, $file3)

Write-Host $MyInvocation.MyCommand.Name $keyfile1 $keyfile2 $file1 $file2 $file3

##--------------------------------------------------------##
## 引数チェック
##--------------------------------------------------------##

if (-Not($keyfile1) -Or -Not($keyfile2) -Or -Not($file1) -Or -Not($file2) -Or -Not($file3)) {
    Write-Host $keyfile1 $keyfile2 $file1 $file2 $file3
    Write-Host "Usage :"$MyInvocation.MyCommand.Name" public_key private_key org_file encrypted_file decrypted_file"
    exit
}


##--------------------------------------------------------##
## 検証対象プログラムの指定
##--------------------------------------------------------##

$cmd_rsa_main = "../../rsa_main_mode_bin.py"
$cmd_filehash = "../../print_FileHash.py"


##--------------------------------------------------------##
## 対象ファイルの事前削除
##--------------------------------------------------------##

if (Test-Path $keyfile1) {
    rm $keyfile1
}

if (Test-Path $keyfile2) {
    rm $keyfile2
}

if (Test-Path $file2) {
    rm $file2
}

if (Test-Path $file3) {
    rm $file3
}


##--------------------------------------------------------##
## 公開鍵／秘密鍵ファイルの生成
##--------------------------------------------------------##

$keyfiles = $keyfile1 + "`r`n" + $keyfile2 + "`r`n"
$keyfiles | python $cmd_rsa_main create_key 


##--------------------------------------------------------##
## 鍵ファイルの内容を表示
##--------------------------------------------------------##

$key1 = Get-Content $keyfile1
$key2 = Get-Content $keyfile2
Write-Host $keyfile1.PadRight(20)":"$key1 -ForegroundColor Yellow
Write-Host $keyfile2.PadRight(20)":"$key2 -ForegroundColor Yellow


##--------------------------------------------------------##
## 暗号化処理
##--------------------------------------------------------##

python $cmd_rsa_main encrypt $file1 $file2 $keyfile1


##--------------------------------------------------------##
## 復号化処理
##--------------------------------------------------------##

python $cmd_rsa_main decrypt $file2 $file3 $keyfile2


##--------------------------------------------------------##
## 変換前ファイルと変換後ファイルのハッシュ値を出力する
##--------------------------------------------------------##

$result1 = python $cmd_filehash $file1
$result3 = python $cmd_filehash $file3

Write-Host $file1.PadRight(20)$result1 -ForegroundColor Cyan
Write-Host $file3.PadRight(20)$result3 -ForegroundColor Cyan


##--------------------------------------------------------##
## 一致／不一致の結果を表示
##--------------------------------------------------------##

if ($result1 -eq $result3) {
    Write-Host "<<Sucess>>" -ForegroundColor Green
}
else {
    Write-Host "<<Failed>>" -ForegroundColor Red
}
