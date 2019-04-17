rm rsa_public.key
rm rsa_private.key
rm test.jpg
rm test.bin

python .\rsa_main_mode_bin.py create_key
python .\rsa_main_mode_bin.py encrypt .\base64_work\image.jpg test.bin .\rsa_public.key
python .\rsa_main_mode_bin.py decrypt .\test.bin test.jpg .\rsa_private.key

python .\print_FileHash.py .\base64_work\image.jpg
python .\print_FileHash.py .\test.jpg
