from Crypto.Cipher import AES
from Libs.CryptoAbstract import Crypto128


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


class AES128(Crypto128):

    def __init__(self, key, mode):
        self.mode = mode

        # key initialization
        self.key = str.encode(key)
        if len(self.key) > 16:
            raise ValueError('Key must be 16 bytes or less')
        elif len(self.key) < 16:
            self.key += str.encode('0') * (16 - len(self.key))

        # AES object initialization (from Crypto.Cipher lib)
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def _encryptblock(self, block128):
        return self.cipher.encrypt(block128)

    def _decryptBlock(self, block128):
        return self.cipher.decrypt(block128)

    def encfile(self, file_path_in, file_path_out):
        file_read = open(file_path_in, 'rb')
        file_write = open(file_path_out, 'wb')
        integer_val = 0

        if self.mode == 'ECB':
            while 1:
                temp = file_read.read(16)
                if not temp:
                    break
                temp = temp if len(temp) == 16 else temp + integer_val.to_bytes((16 - len(temp)), 'big')
                temp_number = self._encryptblock(temp)
                file_write.write(temp_number)
        elif self.mode == 'CBC':
            IV = str.encode('0000000000000000')
            i = 0
            while 1:
                temp = file_read.read(16)
                if not temp:
                    break
                temp = temp if len(temp) == 16 else temp + integer_val.to_bytes((16 - len(temp)), 'big')
                temp = byte_xor(temp, IV)
                IV = self._encryptblock(temp)
                file_write.write(IV)
                i = i + 1

        file_read.close()
        file_write.close()

    def decfile(self, file_path_in, file_path_out):
        file_read = open(file_path_in, 'rb')
        file_write = open(file_path_out, 'wb')
        integer_val = 0

        if self.mode == 'ECB':
            while 1:
                temp = file_read.read(16)
                if not temp:
                    break
                temp = temp if len(temp) == 16 else temp + integer_val.to_bytes((16 - len(temp)), 'big')
                temp_number = self._decryptBlock(temp)
                file_write.write(temp_number)
        elif self.mode == 'CBC':
            IV = str.encode('0000000000000000')
            i = 0
            while 1:
                temp = file_read.read(16)
                if not temp:
                    break
                temp = temp if len(temp) == 16 else temp + integer_val.to_bytes((16 - len(temp)), 'big')
                temp = byte_xor(temp, IV)
                IV = self._decryptBlock(temp)
                file_write.write(IV)
                i = i + 1

        file_read.close()
        file_write.close()
