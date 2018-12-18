__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
import os
import magic
import ntpath
import hashlib


class Identification:

    def __init__(self, _file_path):
        self.__file_path__ = _file_path

    def __extract_file_name_extension(self):
        try:
            _base_name, _file_extension = os.path.splitext(self.__file_path__)
            _file_name = ntpath.basename(self.__file_path__)
            _file_information = {'file_name': _file_name, 'file_extension': _file_extension}
            return True, _file_information
        except:
            return False, 'Failed to identify file type.'

    def __get_magic_value(self):
        try:
            _file_information = {}
            _mime = magic.Magic(mime=True)
            _mime_type = _mime.from_file(self.__file_path__)
            _file_information['mime_info'] = _mime_type
            return True, _file_information
        except:
            return False, 'Failed to identify mime type of file.'

    def calculate_md5sum(self):
        try:
            hash_md5 = hashlib.md5()
            with open(self.__file_path__, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return True, hash_md5.hexdigest()
        except:
            return False, 'Failed to calculate md5sum hash'

    @staticmethod
    def __identify_file_type_mime(_mime_type):
        _file_type = []

        _mime_collection = {'doc': "application/msword", 'dot': "application/msword",
                     'docx': "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                     'dotx': "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
                     'docm': "application/vnd.ms-word.document.macroEnabled.12",
                     'dotm': "application/vnd.ms-word.template.macroEnabled.12", 'xls': "application/vnd.ms-excel",
                     'xlt': "application/vnd.ms-excel", 'xla': "application/vnd.ms-excel",
                     'xlsx': "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                     'xltx': "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
                     'xlsm': "application/vnd.ms-excel.sheet.macroEnabled.12",
                     'xltm': "application/vnd.ms-excel.template.macroEnabled.12",
                     'xlam': "application/vnd.ms-excel.addin.macroEnabled.12",
                     'xlsb': "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
                     'ppt': "application/vnd.ms-powerpoint", 'pot': "application/vnd.ms-powerpoint",
                     'pps': "application/vnd.ms-powerpoint", 'ppa': "application/vnd.ms-powerpoint",
                     'pptx': "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                     'potx': "application/vnd.openxmlformats-officedocument.presentationml.template",
                     'ppsx': "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
                     'ppam': "application/vnd.ms-powerpoint.addin.macroEnabled.12",
                     'pptm': "application/vnd.ms-powerpoint.presentation.macroEnabled.12",
                     'potm': "application/vnd.ms-powerpoint.presentation.macroEnabled.12",
                     'ppsm': "application/vnd.ms-powerpoint.slideshow.macroEnabled.12"}
        for __file_type, __mime_type in _mime_collection.items():
            if _mime_type == __mime_type:
                _file_type.append(__file_type)
        return True, _file_type

    def get_information(self):
        _file_information = {}
        _is_success, _file_info = self.__extract_file_name_extension()
        if _is_success:
            if 'file_name' in _file_info:
                _file_information['file_name'] = _file_info['file_name']
            if 'file_extension' in _file_info:
                _file_information['file_extension'] = _file_info['file_extension']
        _is_success, _hash = self.calculate_md5sum()
        if _is_success:
            _file_information['md5sum'] = _hash
        _is_success, _magic_value = self.__get_magic_value()
        if _is_success:
            _file_information['magic'] = _magic_value['mime_info']
        _is_success, _extension = self.__identify_file_type_mime(_magic_value['mime_info'])
        if _is_success:
            _file_information['extension'] = _extension

        return True, _file_information
