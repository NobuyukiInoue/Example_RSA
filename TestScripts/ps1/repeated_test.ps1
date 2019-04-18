param($keyfile1, $keyfile2, $file1, $file2, $file3)

Write-Host $MyInvocation.MyCommand.Name $keyfile1 $keyfile2 $file1 $file2 $file3

##--------------------------------------------------------##
## �����`�F�b�N
##--------------------------------------------------------##

if (-Not($keyfile1) -Or -Not($keyfile2) -Or -Not($file1) -Or -Not($file2) -Or -Not($file3)) {
    Write-Host $keyfile1 $keyfile2 $file1 $file2 $file3
    Write-Host "Usage :"$MyInvocation.MyCommand.Name" public_key private_key org_file encrypted_file decrypted_file"
    exit
}


##--------------------------------------------------------##
## ���ؑΏۃv���O�����̎w��
##--------------------------------------------------------##

$cmd_rsa_main = "../../rsa_main_mode_bin.py"
$cmd_filehash = "../../print_FileHash.py"


##--------------------------------------------------------##
## �Ώۃt�@�C���̎��O�폜
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
## ���J���^�閧���t�@�C���̐���
##--------------------------------------------------------##

$keyfiles = $keyfile1 + "`r`n" + $keyfile2 + "`r`n"
$keyfiles | python $cmd_rsa_main create_key 


##--------------------------------------------------------##
## ���t�@�C���̓��e��\��
##--------------------------------------------------------##

$key1 = Get-Content $keyfile1
$key2 = Get-Content $keyfile2
Write-Host $keyfile1.PadRight(20)":"$key1 -ForegroundColor Yellow
Write-Host $keyfile2.PadRight(20)":"$key2 -ForegroundColor Yellow


##--------------------------------------------------------##
## �Í�������
##--------------------------------------------------------##

python $cmd_rsa_main encrypt $file1 $file2 $keyfile1


##--------------------------------------------------------##
## ����������
##--------------------------------------------------------##

python $cmd_rsa_main decrypt $file2 $file3 $keyfile2


##--------------------------------------------------------##
## �ϊ��O�t�@�C���ƕϊ���t�@�C���̃n�b�V���l���o�͂���
##--------------------------------------------------------##

$result1 = python $cmd_filehash $file1
$result3 = python $cmd_filehash $file3

Write-Host $file1.PadRight(20)$result1 -ForegroundColor Cyan
Write-Host $file3.PadRight(20)$result3 -ForegroundColor Cyan


##--------------------------------------------------------##
## ��v�^�s��v�̌��ʂ�\��
##--------------------------------------------------------##

if ($result1 -eq $result3) {
    Write-Host "<<Sucess>>" -ForegroundColor Green
}
else {
    Write-Host "<<Failed>>" -ForegroundColor Red
}
