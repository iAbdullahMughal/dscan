__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
from core.analysis.identification import *


class ObjectInformation:

    def __init__(self, object_path=None):
        if object_path:
            self.__file_path__ = object_path
        else:
            self.__file_path__ = None

    """
    @TODO: Following attributes need to be added for embedded objects 
    1. File name
    2. File Size
    3. File Type
    4. It txt then what is the type of txt file
    5. hashs    
    """

    def extract_information(self, object_path=None):
        sample_information = {}
        if object_path:
            self.__file_path__ = object_path

        if not self.__file_path__:
            return False, 'No object path was passed as parameter.'

        filesize = FileSize(self.__file_path__)
        return_code, file_size = filesize.do_size_calculation()
        if return_code:
            sample_information['file_size'] = file_size['file_size']
            sample_information['file_size_readable'] = file_size['file_size_readable']

        filetype = FileIdentify(self.__file_path__)
        return_code, file_type = filetype.do_file_identify()
        file_type_tags = []
        if return_code:
            for tag in file_type['file_type_tags']:
                if tag not in ('file', 'text', 'non-executable', 'binary') and tag:
                    file_type_tags.append(tag)
        sample_information['identify'] = file_type_tags

        magictype = FileMagic(self.__file_path__)
        return_code, magic_info = magictype.do_magic_identification()
        if return_code:
            if magic_info['mime_file_type']:
                sample_information['mime'] = magic_info['mime']
                sample_information['mime_file_type'] = magic_info['mime_file_type']

        filehashs = CalculateHash(self.__file_path__)
        return_code, file_hashs = filehashs.do_hash_calculation()
        if return_code:
            sample_information['md5sum'] = file_hashs['md5sum']
            sample_information['sha1sum'] = file_hashs['sha1sum']
            sample_information['sha256sum'] = file_hashs['sha256sum']
        print(sample_information)
