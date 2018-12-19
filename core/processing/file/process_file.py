__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from config.config import LocationConfig
import json
from core.modules.analysis.file_operation import FileOperation
from core.modules.macro.extract_macro import ExtractMacro
from core.processing.macro.code_normalization import CodeNormalization


class ProcessFile:

    def __init__(self, _file_path):
        self.__file_path__ = _file_path

    @staticmethod
    def __create_json(_md5sum, _json_content):
        """
        This function create json file for analyzed sample by the tool on system.
        :param _md5sum: md5sum of sample
        :param _json_content: json content created by tool
        :return: tuple
            boolean, string of result
        """
        try:
            with open(LocationConfig.JSON_LOCATION + _md5sum + ".json", 'w') as json_file:
                json.dump(_json_content, json_file)
            return True, 'Json created.'
        except Exception as e:
            return False, str(e)

    def __do_extraction(self):
        """
        This function performs macro and code extraction from the file
        :return:
        """
        obj = ExtractMacro()
        code_dictionary = {}
        is_success, result = obj.do_macro_extraction(self.__file_path__)
        if is_success:
            normalized_code = CodeNormalization(result)
            is_success, code_dictionary = normalized_code.do_normalization()
            code_dictionary['extracted_macro'] = result
            return True, code_dictionary
        return True, code_dictionary

    def process_file(self):
        _hash_result = ''
        _identification = FileOperation(self.__file_path__)
        _is_file, _file_information = _identification.get_information()
        if _is_file:
            _hash_result = _file_information['md5sum']
            is_success, _json_content = self.__do_extraction()
            if 'complete_code' in _json_content:
                _file_information['has_macro'] = True
            else:
                _file_information['has_macro'] = False
            _file_information.update(_json_content)
            if is_success:
                _is_success, _returned_message = self.__create_json(_hash_result, _file_information)
            return True, _hash_result

        else:
            return False, 'Failed to store information.'
