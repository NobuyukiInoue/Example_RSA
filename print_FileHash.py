import hashlib
import os
import sys


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 1:
        exit_msg(argv[0])

    if not os.path.exists(argv[1]):
        print("%s not found." %argv[1])
        exit(0)

    f = open(argv[1],'rb')
    BinaryData = f.read()
    f.close()

    if argc >= 3:
        if argv[2] == "SHA2":
            SHA2 = hashlib.md5(BinaryData).hexdigest()
            print('SHA2 :', SHA2)
        if argv[2] == "SHA1":
            SHA1 = hashlib.sha1(BinaryData).hexdigest()
            print('SHA1 :', SHA1)
        elif argv[2] == "MD5":
            MD5 = hashlib.md5(BinaryData).hexdigest()
            print('MD5 :', MD5)
        else:
            print("%s not found." %argv[2])
    else:
        SHA2 = hashlib.md5(BinaryData).hexdigest()
        print('SHA2 :', SHA2)

def exit_msg(argv0):
    print("Usage: python %s [target_file] [SHA1 | MD5]" %argv0)
    exit(0)


if __name__ == "__main__":
    main()
