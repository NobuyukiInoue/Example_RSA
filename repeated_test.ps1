param($public_key, $private_key, $file1, $file2, $file3)

Write-Host $MyInvocation.MyCommand.Name $public_key $private_key $file1 $file2 $file3

if (-Not($public_key) -Or -Not($private_key) -Or -Not($file1) -Or -Not($file2) -Or -Not($file3)) {
    Write-Host $public_key $private_key $file1 $file2 $file3
    Write-Host "Usage :"$MyInvocation.MyCommand.Name" public_key private_key org_file encrypted_file decrypted_file"
    exit
}

if (Test-Path $public_key) {
    rm $public_key
}

if (Test-Path $private_key) {
    rm $private_key
}

if (Test-Path $file2) {
    rm $file2
}

if (Test-Path $file3) {
    rm $file3
}

python ./rsa_main_mode_bin.py create_key

$key1 = Get-Content $public_key
$key2 = Get-Content $private_key
Write-Host $public_key.PadRight(20)":"$key1 -ForegroundColor Yellow
Write-Host $private_key.PadRight(20)":"$key2 -ForegroundColor Yellow

python ./rsa_main_mode_bin.py encrypt $file1 $file2 $public_key
python ./rsa_main_mode_bin.py decrypt $file2 $file3 $private_key

$result1 = python ./print_FileHash.py $file1
$result2 = python ./print_FileHash.py $file3

Write-Host $file1.PadRight(30)$result1 -ForegroundColor Cyan
Write-Host $file2.PadRight(30)$result2 -ForegroundColor Cyan

if ($result1 -eq $result2) {
    Write-Host "Sucess." -ForegroundColor Green
}
else {
    Write-Host "Failed." -ForegroundColor Red
}
