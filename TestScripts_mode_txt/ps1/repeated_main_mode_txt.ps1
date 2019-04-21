$cmd = "./test_mode_txt.ps1"
$keyfile1 = "./public.key"
$keyfile2 = "./private.key"
$file1 = "./original_sjis.txt"
$file2 = "./test.bin"
$file3 = "./test.txt"
$code = "sjis"

$loopCount = 10

Write-Host "#### encypt(public_key) --> decrypt(private_key) ###" -ForegroundColor Magenta

for ($i = 0; $i -lt $loopCount; $i++) {
    &$cmd $keyfile1 $keyfile2 $file1 $file2 $file3 $code
}


Write-Host "#### encypt(private_key) --> decrypt(public_key) ###" -ForegroundColor Magenta

for ($i = 0; $i -lt $loopCount; $i++) {
    &$cmd $keyfile1 $keyfile2 $file1 $file2 $file3 $code False
}
