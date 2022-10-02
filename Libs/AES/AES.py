from Crypto.Cipher import AES

from ..CryptoAbstract import Crypto128


class AES128(Crypto128):
    def __init__(self, secretkey128):
        pass

    def keygen(self):
        pass

    def encryptblock(self, block128):
        pass

    def decryptBlock(self, block128):
        pass

    def encfile(self, file, secretKey, MODE):
        pass

    def decfile(self, file, secretKey, MODE):
        pass


cipher = AES128()
