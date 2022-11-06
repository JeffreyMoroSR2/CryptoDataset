from Crypto.Cipher import DES
from Libs.CryptoAbstract import Crypto64


class Single_DES(Crypto64):

    def __init__(self, key, mode):
        self.mode = mode

        # key initialization
        self.key = str.encode(key)
        if len(self.key) > 8:
            raise ValueError('Key must be 8 bytes or less')
        elif len(self.key) < 8:
            self.key += str.encode('0') * (8 - len(self.key))

        # DES object initialization (from Crypto.Cipher lib)
        self.cipher = DES.new(self.key, DES.MODE_ECB)

    def _encryptblock(self, block64):
        return self.cipher.encrypt(block64)

    def _decryptBlock(self, block64):
        return self.cipher.decrypt(block64)

    def encfile(self, file_path_in, file_path_out):
        file_read = open(file_path_in, 'rb')
        file_write = open(file_path_out, 'wb')
        integer_val = 0

        if self.mode == 'ECB':
            while 1:
                temp = file_read.read(8)
                if not temp:
                    break
                temp = temp if len(temp) == 8 else temp + integer_val.to_bytes((8 - len(temp)), 'big')
                temp_number = self._encryptblock(temp)
                file_write.write(temp_number)
        elif self.mode == 'CBC':
            # TODO: implement CBC
            while 1:
                temp = file_read.read(8)
                if not temp:
                    break
                file_write.write(temp)

        file_read.close()
        file_write.close()

    def decfile(self, file_path_in, file_path_out):
        file_read = open(file_path_in, 'rb')
        file_write = open(file_path_out, 'wb')
        integer_val = 0

        if self.mode == 'ECB':
            while 1:
                temp = file_read.read(8)
                if not temp:
                    break
                temp = temp if len(temp) == 8 else temp + integer_val.to_bytes((8 - len(temp)), 'big')
                temp_number = self._decryptBlock(temp)
                file_write.write(temp_number)
        elif self.mode == 'CBC':
            # TODO: implement CBC
            while 1:
                temp = file_read.read(8)
                if not temp:
                    break
                file_write.write(temp)

        file_read.close()
        file_write.close()
