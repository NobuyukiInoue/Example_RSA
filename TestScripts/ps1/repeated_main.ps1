$cmd = "./repeated_test.ps1"
$keyfile1 = "./key1.key"
$keyfile2 = "./key2.key"
$file1 = "./image.jpg"
$file2 = "./test.bin"
$file3 = "./test.jpg"

Write-Host "#### encypt(public_key) --> decrypt(private_key) ###" -ForegroundColor Red

for ($i = 0; $i -lt 10; $i++) {
    # Write-Host $cmd $keyfile1 $keyfile2 $file1 $file2 $file3
    &$cmd $keyfile1 $keyfile2 $file1 $file2 $file3
}


Write-Host "#### encypt(private_key) --> decrypt(public_key) ###" -ForegroundColor Red

for ($i = 0; $i -lt 10; $i++) {
    # Write-Host $cmd $keyfile2 $keyfile1 $file1 $file2 $file3 2
    &$cmd $keyfile2 $keyfile1 $file1 $file2 $file3
}
