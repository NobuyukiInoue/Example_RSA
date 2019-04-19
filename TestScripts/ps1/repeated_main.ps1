$cmd = "./repeated_test.ps1"
$keyfile1 = "./public.key"
$keyfile2 = "./private.key"
$file1 = "./image.jpg"
$file2 = "./test.bin"
$file3 = "./test.jpg"

Write-Host "#### encypt(public_key) --> decrypt(private_key) ###" -ForegroundColor Magenta

for ($i = 0; $i -lt 10; $i++) {
    &$cmd $keyfile1 $keyfile2 $file1 $file2 $file3
}


Write-Host "#### encypt(private_key) --> decrypt(public_key) ###" -ForegroundColor Magenta

for ($i = 0; $i -lt 10; $i++) {
    &$cmd $keyfile1 $keyfile2 $file1 $file2 $file3 False
}
