import sys
import os
from Libs.env import Cryptolist, ModeList


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
            print('Supported methods: \n')
            for i in Cryptolist:
                for key, values in i.items():
                    print(key, '\n')
            return
        elif argv[0] == '-m':
            print('Supported modes: \n')
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
        for i in Cryptolist:
            for key, values in i.items():
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


if __name__ == "__main__":
    main(sys.argv[1:])
