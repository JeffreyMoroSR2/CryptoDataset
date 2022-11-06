from Crypto.Cipher import Salsa20
from Libs.CryptoAbstract import Crypto_Stream


class Salsa_20(Crypto_Stream):

    def __init__(self, key, mode):
        self.mode = mode

        # key initialization
        self.key = str.encode(key)
        if len(self.key) > 32:
            raise ValueError('Key must be in range of 16-32 bytes')
        elif len(self.key) < 16:
            self.key += str.encode('0') * (16 - len(self.key))

        # Salsa20 object initialization (from Crypto.Cipher lib)
        self.cipher = Salsa20.new(self.key)
        self.nonce = self.cipher.nonce

    def _encrypt(self, data):
        return self.nonce + self.cipher.encrypt(data)

    def _decrypt(self, data):
        data_nonce = data[:8]
        enc_data = data[8:]
        cipher_dec = Salsa20.new(key=self.key, nonce=data_nonce)
        return cipher_dec.decrypt(enc_data)

    def encfile(self, file_path_in, file_path_out):
        file_read = open(file_path_in, 'rb')
        file_write = open(file_path_out, 'wb')
        integer_val = 0
        while 1:
            temp = file_read.read()
            if not temp:
                break
            temp = temp if len(temp) == 1 else temp + integer_val.to_bytes((1 - len(temp)), 'big')
            temp_number = self._encrypt(temp)
            file_write.write(temp_number)

    def decfile(self, file_path_in, file_path_out):
        file_read = open(file_path_in, 'rb')
        file_write = open(file_path_out, 'wb')
        integer_val = 0
        while 1:
            temp = file_read.read(1)
            if not temp:
                break
            temp = temp if len(temp) == 1 else temp + integer_val.to_bytes((1 - len(temp)), 'big')
            temp_number = self._decrypt(temp)
            file_write.write(temp_number)
