__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from config.config import LocationConfig
import json
from core.process.identification import Identification
from core.modules.extract_macro import ExtractMacro
from core.modules.normalize_code import NormalizeCode


class ProcessFile:

    def __init__(self, _file_path):
        self.__file_path__ = _file_path

    @staticmethod
    def __create_json(_md5sum, _json_content):
        try:
            with open(LocationConfig.JSON_LOCATION + _md5sum + ".json", 'w') as json_file:
                json.dump(_json_content, json_file)
            return True, 'Json created.'
        except Exception as e:
            return False, str(e)

    def __do_extraction(self):
        obj = ExtractMacro()
        code_dictionary = {}
        is_success, result = obj.do_macro_extraction(self.__file_path__)
        if is_success:
            normalized_code = NormalizeCode(result)
            is_success, code_dictionary = normalized_code.get_data()
            code_dictionary['extracted_macro'] = result
            return True, code_dictionary
        return True, code_dictionary

    def process_file(self):
        _identification = Identification(self.__file_path__)
        is_success, _hash_result = _identification.calculate_md5sum()
        _is_file, _file_information = _identification.get_information()
        if _is_file:
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
