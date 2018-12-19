__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

import hashlib


class HashCalculation:
    def __init__(self, _file_path):
        self.__file_path__ = _file_path

    def calculate_md5sum(self):
        try:
            hash_md5 = hashlib.md5()
            with open(self.__file_path__, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return True, hash_md5.hexdigest()
        except:
            return False, 'Failed to calculate md5sum hash'
