from Crypto.Cipher import DES3
from Libs.CryptoAbstract import Crypto64


class Triple_DES(Crypto64):

    def __init__(self, key, mode):
        self.mode = mode

        # key initialization
        self.key = str.encode(key)
        if len(self.key) > 24:
            raise ValueError('Key must be 24 bytes or less')
        elif len(self.key) < 24:
            self.key += str.encode('0') * (24 - len(self.key))

        # DES3 object initialization (from Crypto.Cipher lib)
        self.cipher = DES3.new(self.key, DES3.MODE_ECB)

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
