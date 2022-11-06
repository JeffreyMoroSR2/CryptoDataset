import sys
import os
from Libs.env import Cryptolist, ModeList

"""Importing available modules"""
from Libs.AES.AES128 import AES128
from Libs.AES.AES192 import AES192
from Libs.AES.AES256 import AES256
from Libs.DES.Single_DES import Single_DES
from Libs.DES.Triple_DES import Triple_DES
from Libs.CAST.CAST import CAST128
from Libs.RC.RC2 import RC2

"""Command line functionality"""


def main(argv):
    n = len(argv)
    if n == 0:
        print('Usage: python main.py -[enc/dec] [Enc/Dec method] [Mode] [Key] [InFile] [OutFile] \n'
              'To see supported methods use -> python main.py -s \n'
              'To see supported modes use -> python main.py -m')
        return
    elif n == 1:
        if argv[0] == '-h':
            print('Usage: python main.py -[enc/dec] [Enc/Dec method] [Mode] [Key] [InFile] [OutFile] \n'
                  'To see supported methods use -> python main.py -s \n'
                  'To see supported modes use -> python main.py -m')
            return
        elif argv[0] == '-s':
            print('Supported methods:')
            for key, values in Cryptolist.items():
                print(key)
            return
        elif argv[0] == '-m':
            print('Supported modes:')
            for i in ModeList:
                print(i)
            return
        else:
            print('Wrong input, please try again or use -> python main.py -h')
            return
    elif n == 6:
        if argv[0] != '-enc' and argv[0] != '-dec':
            print('Choose -enc or -dec')
            return

        flag = False
        for key, values in Cryptolist.items():
            if argv[1] == key:
                flag = True
                break
            if flag:
                break
        if not flag:
            print("Method", argv[1], "doesn't exist")
            return

        if argv[2] not in ModeList:
            print("Mode", argv[2], "doesn't exist")
            return

        if not os.path.isfile(argv[4]):
            print("File", argv[4], "doesn't exist")
            return
    else:
        print('Wrong input, please try again or use -> python main.py -h')
        return

    if argv[0] == '-enc':
        encryptor(argv[1], argv[2], argv[3], argv[4], argv[5])
    else:
        decryptor(argv[1], argv[2], argv[3], argv[4], argv[5])


def encryptor(Method, Mode, Key, in_file, out_file):
    encrypt = eval(Cryptolist[Method])(Key, Mode)
    encrypt.encfile(in_file, out_file)


def decryptor(Method, Mode, Key, in_file, out_file):
    decrypt = eval(Cryptolist[Method])(Key, Mode)
    decrypt.decfile(in_file, out_file)


if __name__ == "__main__":
    main(sys.argv[1:])
