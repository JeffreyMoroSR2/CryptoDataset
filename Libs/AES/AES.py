from Crypto.Cipher import AES

from CryptoAbstract import Crypto128


class AES128(Crypto128):
    def __init__(self, secretkey128):
        self.secretkey128 = secretkey128

    def keygen(self):
        self.secretkey128 = bytearray(self.secretkey128)
        if len(self.secretkey128) > 16:
            print(self.secretkey128)
            self.secretkey128 = self.secretkey128[len(self.secretkey128) - 16:]
            print(len(self.secretkey128))

    def encryptblock(self, block128):
        pass

    def decryptBlock(self, block128):
        pass

    def encfile(self, file, secretKey, MODE):
        pass

    def decfile(self, file, secretKey, MODE):
        pass


cipher = AES128(16)
cipher.keygen()