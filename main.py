from abc import ABC, abstractmethod


class Crypto128(ABC):
    @abstractmethod
    def keygen(self):
        pass

    @abstractmethod
    def encryptblock(self, block128):
        pass

    @abstractmethod
    def decryptBlock(self, block128):
        pass

    @abstractmethod
    def encfile(self, file, secretKey, MODE):
        pass

    @abstractmethod
    def decfile(self, file, secretKey, MODE):
        pass
