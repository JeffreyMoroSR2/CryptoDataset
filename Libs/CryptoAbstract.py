from abc import ABC, abstractmethod


class Crypto128(ABC):

    @abstractmethod
    def _encryptblock(self, block128):
        pass

    @abstractmethod
    def _decryptBlock(self, block128):
        pass

    @abstractmethod
    def encfile(self, file_path_in, file_path_out):
        pass

    @abstractmethod
    def decfile(self, file_path_in, file_path_out):
        pass
