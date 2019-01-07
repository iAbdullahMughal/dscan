__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

import hashlib


class CalculateHash:
    def __init__(self, file_path):
        self.__file_path__ = file_path
        self.__results__ = {}
        self.__error__ = []

    def __md5sum(self):
        try:
            hash_md5 = hashlib.md5()
            with open(self.__file_path__, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            self.__results__['md5sum'] = hash_md5.hexdigest()
        except Exception as e:
            __exception = 'Failed to calculate md5sum. ' + str(e)
            self.__error__.append(__exception)

    def __sha256sum(self):
        try:
            hash_sha256 = hashlib.sha256()
            with open(self.__file_path__, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            self.__results__['sha256sum'] = hash_sha256.hexdigest()
        except Exception as e:
            __exception = 'Failed to calculate md5sum. ' + str(e)
            self.__error__.append(__exception)

    def __sha1sum(self):
        try:
            hash_sha1 = hashlib.sha1()
            with open(self.__file_path__, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha1.update(chunk)
            self.__results__['sha1sum'] = hash_sha1.hexdigest()
        except Exception as e:
            __exception = 'Failed to calculate md5sum. ' + str(e)
            self.__error__.append(__exception)

    def do_hash_calculation(self, file_path=None):

        if file_path:
            self.__file_path__ = file_path

        if not self.__file_path__:
            self.__error__.append('No file path was given.')
            self.__results__['error'] = self.__error__
            return False, self.__results__

        self.__md5sum()
        self.__sha1sum()
        self.__sha256sum()
        self.__results__['error'] = self.__error__
        if self.__results__['error']:
            return False, self.__results__
        return True, self.__results__
