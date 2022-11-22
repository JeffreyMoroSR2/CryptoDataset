from Crypto.Cipher import Salsa20
from Libs.CryptoAbstract import Crypto_Stream


class Salsa_20(Crypto_Stream):

    def __init__(self, key, mode, nonce='nonce_df', block_length=8):
        self.mode = mode
        self.nonce = str.encode(nonce)
        if len(self.nonce) != 8:
            raise ValueError('Nonce should be 8 bytes')

        self.block_length = block_length
        if self.block_length != 8 and self.block_length != 16 and self.block_length != 32:
            raise ValueError('Block should be 8/16/32 bytes')

        # key initialization
        self.key = str.encode(key)
        if len(self.key) != 32:
            raise ValueError('Key must be 32 bytes')

        self.cipher = Salsa20.new(self.key, nonce=self.nonce)

    def _encrypt(self, data, flag=False):
        if flag:
            return data
        return self.cipher.encrypt(data)

    def _decrypt(self, data):
        return self.cipher.decrypt(data)

    def encfile(self, file_path_in, file_path_out):
        file_read = open(file_path_in, 'rb')
        file_write = open(file_path_out, 'wb')
        integer_val = 0

        while 1:
            temp = file_read.read(self.block_length)
            if not temp:
                nonce = self._encrypt(self.nonce, True)
                file_write.write(nonce)
                break
            temp = temp if len(temp) == self.block_length else \
                temp + integer_val.to_bytes((self.block_length - len(temp)), 'big')
            temp_number = self._encrypt(temp)
            file_write.write(temp_number)

    def decfile(self, file_path_in, file_path_out):
        file_read = open(file_path_in, 'rb')
        file_write = open(file_path_out, 'wb')
        integer_val = 0

        # file_write.write(file_read.read()[:8])
        while 1:
            temp = file_read.read(self.block_length)
            if not temp:
                break
            temp = temp if len(temp) == self.block_length else \
                temp + integer_val.to_bytes((self.block_length - len(temp)), 'big')
            temp_number = self._decrypt(temp)
            file_write.write(temp_number)
