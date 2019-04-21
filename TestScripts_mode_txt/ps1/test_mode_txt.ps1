param($keyfile1, $keyfile2, $file1, $file2, $file3, $code, $mode)

Write-Host "args ="$MyInvocation.MyCommand.Name $keyfile1 $keyfile2 $file1 $file2 $file3 $code $mode

##--------------------------------------------------------##
## 引数チェック
##--------------------------------------------------------##

if (-Not($keyfile1) -Or -Not($keyfile2) -Or -Not($file1) -Or -Not($file2) -Or -Not($file3)) {
    Write-Host $keyfile1 $keyfile2 $file1 $file2 $file3
    Write-Host "Usage :"$MyInvocation.MyCommand.Name" public_key private_key org_file encrypted_file decrypted_file [mode]"
    exit
}

if (-Not($code)) {
    $code = "utf8"
}


if (-Not($mode)) {
    $mode = $TRUE
}
else {
    if ($mode -match "TRUE" -Or $mode -match "True" -Or $mode -match "true") {
        $mode = $TRUE
    }
    else {
        $mode = $FALSE
    }
}


##--------------------------------------------------------##
## 検証対象プログラムの指定
##--------------------------------------------------------##

$cmd_rsa_main = "../../rsa_main_mode_txt.py"
$cmd_filehash = "../../print_FileHash.py"


##--------------------------------------------------------##
## 対象ファイルの事前削除
##--------------------------------------------------------##

if (Test-Path $keyfile1) {
    Remove-Item $keyfile1
}

if (Test-Path $keyfile2) {
    Remove-Item $keyfile2
}

if (Test-Path $file2) {
    Remove-Item $file2
}

if (Test-Path $file3) {
    Remove-Item $file3
}


##--------------------------------------------------------##
## 公開鍵／秘密鍵ファイルの生成
##--------------------------------------------------------##

$keyfiles = $keyfile1 + "`n" + $keyfile2 + "`n"

Write-Host "Execute: python"$cmd_rsa_main" create_key"
$keyfiles | python $cmd_rsa_main create_key > $NULL


##--------------------------------------------------------##
## 暗号化処理
##--------------------------------------------------------##

if ($mode) {
    ## 公開鍵で暗号化
    Write-Host "Execute: python $cmd_rsa_main encrypt $file1 $keyfile1 $code"
    python $cmd_rsa_main encrypt $file1 $keyfile1 $code > $file2".unicode"
}
else {
    ## 秘密鍵で暗号化
    Write-Host "Execute: python $cmd_rsa_main encrypt $file1 $keyfile2 $code"
    python $cmd_rsa_main encrypt $file1 $keyfile2 $code > $file2".unicode"
}


get-content -Encoding Unicode $file2".unicode" | Set-Content $file2 -Encoding OEM
Remove-Item $file2".unicode"


##--------------------------------------------------------##
## 復号処理
##--------------------------------------------------------##

if ($mode) {
    ## 秘密鍵で復号
    Write-Host "Execute: python $cmd_rsa_main decrypt $file2 $keyfile2 $code"
    python $cmd_rsa_main decrypt $file2 $keyfile2 $code > $file3".unicode"
}
else {
    ## 公開鍵で復号
    Write-Host "Execute: python $cmd_rsa_main decrypt $file2 $keyfile1 $code"
    python $cmd_rsa_main decrypt $file2 $keyfile1 $code > $file3".unicode"
}

get-content -Encoding Unicode $file3".unicode" | Set-Content $file3 -Encoding OEM
Remove-Item $file3".unicode"



##--------------------------------------------------------##
## 鍵ファイルの内容を表示
##--------------------------------------------------------##

$key1 = Get-Content $keyfile1
$key2 = Get-Content $keyfile2
Write-Host $keyfile1.PadRight(20)":"$key1 -ForegroundColor Yellow
Write-Host $keyfile2.PadRight(20)":"$key2 -ForegroundColor Yellow


##--------------------------------------------------------##
## 暗号化前ファイルと復号後ファイルを出力する
##--------------------------------------------------------##

Write-Host "###### 暗号化前:"$file1" ######" -ForegroundColor Cyan
Get-Content $file1
Write-Host "###### 復号後  :"$file3" ######" -ForegroundColor Cyan
Get-Content $file3
Write-Host "####################" -ForegroundColor Cyan
