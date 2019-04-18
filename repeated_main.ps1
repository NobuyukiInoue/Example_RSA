$cmd = "./repeated_test.ps1"
$public_key = "./rsa_public.key"
$private_key = "./rsa_private.key"
$file1 = "./base64_work/image.jpg"
$file2 = "./test.bin"
$file3 = "./test.jpg"

for ($i = 0; $i -lt 10; $i++) {
    # Write-Host $cmd $public_key $private_key $file1 $file2 $file3
    &$cmd $public_key $private_key $file1 $file2 $file3
}
