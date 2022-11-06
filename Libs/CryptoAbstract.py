from abc import ABC, abstractmethod


class Crypto64(ABC):

    @abstractmethod
    def _encryptblock(self, block64):
        pass

    @abstractmethod
    def _decryptBlock(self, block64):
        pass

    @abstractmethod
    def encfile(self, file_path_in, file_path_out):
        pass

    @abstractmethod
    def decfile(self, file_path_in, file_path_out):
        pass


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


class Crypto192(ABC):

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


class Crypto256(ABC):

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


class Crypto_Stream(ABC):

    @abstractmethod
    def _encrypt(self, data):
        pass

    @abstractmethod
    def _decrypt(self, data):
        pass

    @abstractmethod
    def encfile(self, file_path_in, file_path_out):
        pass

    @abstractmethod
    def decfile(self, file_path_in, file_path_out):
        pass
