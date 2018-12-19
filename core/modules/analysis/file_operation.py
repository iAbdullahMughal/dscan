__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
from core.processing.identification.hash_calculation import HashCalculation
from core.processing.identification.file_name import FileName
from core.processing.identification.file_type import FileType


class FileOperation:

    def __init__(self, _file_path):
        self.__file_path__ = _file_path

    def get_information(self):
        _file_information = {}

        obj_hash = HashCalculation(self.__file_path__)
        _is_success, _hash = obj_hash.calculate_md5sum()
        if _is_success:
            _file_information['md5sum'] = _hash

        obj_file_name = FileName(self.__file_path__)
        _is_success, _file_info = obj_file_name.extract_file_name_extension()
        if _is_success:
            if 'file_name' in _file_info:
                _file_information['file_name'] = _file_info['file_name']
            if 'file_extension' in _file_info:
                _file_information['file_extension'] = _file_info['file_extension']

        obj_file_type = FileType(self.__file_path__)
        _is_success, _magic_value = obj_file_type.get_magic_value()
        if _is_success:
            _file_information['magic'] = _magic_value['mime_info']
        _is_success, _extension = obj_file_type.identify_file_type_mime(_magic_value['mime_info'])
        if _is_success:
            _file_information['extension'] = _extension

        return True, _file_information
