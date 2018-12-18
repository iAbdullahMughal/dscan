__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

"""
code snippet from https://github.com/MalwareCantFly/Vba2Graph/blob/master/vba2graph.py
"""
from core import ProjectConfig
import re


class NormalizeCode:

    def __init__(self, _macro_code):
        self.__macro_code__ = _macro_code
        self.__non_anomalies_code__ = ''
        self.__macro_functions__ = {}
        self.__macro_property__ = {}

    def __remove_anomalies(self):

        _macro_content = self.__macro_code__

        # Replace tab and new line with new line
        _macro_content = _macro_content.replace("\r\n", ProjectConfig.LINE_SEPARATOR)
        _macro_content = _macro_content.replace(" _" + ProjectConfig.LINE_SEPARATOR, " ")

        # Converted macro code strings into list
        _macro_content_list = _macro_content.split(ProjectConfig.LINE_SEPARATOR)

        _removed_whitespaces = []
        # Looping through macro code to ignore all whitespaces between macro code
        for __vba_line in _macro_content_list:
            __vba_line = " ".join(__vba_line.split())
            # Ignoring all whitespaces in macro code
            if __vba_line == "":
                continue
            _removed_whitespaces.append(__vba_line)

        _remove_meta = []
        for __vba_line in _removed_whitespaces:
            # Removing Attribute and ' from the code
            if __vba_line.startswith("Attribute") or __vba_line.startswith("'"):
                continue
            _inline_comment_pos = __vba_line.find(" '")
            if _inline_comment_pos > -1:
                if __vba_line.find('"', _inline_comment_pos) < 0:
                    _inline_comment_pos = _inline_comment_pos
                    __vba_line = __vba_line[:_inline_comment_pos]
            _remove_meta.append(__vba_line)

        _remove_indentation = []
        # Removing line indentation from code
        for __vba_line in _remove_meta:
            __vba_line = __vba_line.replace('" & "', "")
            _remove_indentation.append(__vba_line)

        self.__non_anomalies_code__ = _remove_indentation

    def __extract_function(self):
        _vba_functions = {}
        _function_code = False
        _function_name = ""
        for __vba_code_line in self.__non_anomalies_code__:
            if " Lib " in __vba_code_line and ' Alias ' in __vba_code_line and not _function_code:
                if " Function " in __vba_code_line:
                    __function_type = " Function "
                else:
                    __function_type = " Sub "

                __function_name = __vba_code_line[__vba_code_line.find(__function_type) + len(
                    __function_type):__vba_code_line.find(" Lib ")]
                __system_call = __vba_code_line[
                                __vba_code_line.find(" Alias \"") + len(" Alias \""):__vba_code_line.find(
                                    "\" (",
                                    __vba_code_line.find(" Alias \"") + len(" Alias \""))]
                _function_name = __function_name

                if "libc.dylib" in __vba_code_line:
                    _function_name += "(Mac)"
                _vba_functions[_function_name] = "It's function calling windows's " + __system_call
                continue
            if " Lib " in __vba_code_line and not _function_code:
                if " Function " in __vba_code_line:
                    __function_type = " Function "
                else:
                    __function_type = " Sub "
                _function_name = __vba_code_line[__vba_code_line.find(__function_type) + len(
                    __function_type):__vba_code_line.find(" Lib ")]

                if "libc.dylib" in __vba_code_line:
                    _function_name += "(Mac)"

                _vba_functions[_function_name] = "It's custom defined function " + _function_name
                continue
            _function_start_position = max(__vba_code_line.find("Sub "), __vba_code_line.find("Function "))
            _function_start = False
            if __vba_code_line.startswith("Sub") or __vba_code_line.startswith(
                    "Function") or __vba_code_line.startswith(
                "Private") or __vba_code_line.startswith("Public"):
                _function_start = True

            _function_end = __vba_code_line.startswith("End Sub") or __vba_code_line.startswith("End Function")
            if _function_end:
                _function_code = False
                continue
            elif _function_start and _function_start_position > -1:
                _function_code = True
                if "Function " in __vba_code_line:
                    _function_name = __vba_code_line[(
                                                             _function_start_position + len(
                                                         "Function ")):__vba_code_line.find("(")]
                elif "Sub " in __vba_code_line:
                    _function_name = __vba_code_line[(
                                                             _function_start_position + len(
                                                         "Sub ")):__vba_code_line.find("(")]
                else:
                    print("Error parsing function name")
            elif _function_code:
                if _function_name in _vba_functions:
                    _vba_functions[_function_name] += ProjectConfig.LINE_SEPARATOR + __vba_code_line
                else:
                    _vba_functions[_function_name] = __vba_code_line
            else:
                pass
            self.__macro_functions__ = _vba_functions

    def __extract_properties(self):
        _macro_property = {}
        _is_property = False
        _property_name = ""

        for _vba_code in self.__non_anomalies_code__:
            __property_start_position = max(_vba_code.find("Property Let "), _vba_code.find("Property Get "))
            __property_end_position = _vba_code.startswith("End Property")
            if __property_end_position:
                _is_property = False
                continue
            elif __property_start_position > -1:
                _is_property = True
                if "Property Let " in _vba_code or "Property Get " in _vba_code:
                    _property_name = _vba_code[(
                                                       __property_start_position + len("Property Let ")):_vba_code.find(
                        "(")] + " (Property)"
                else:
                    print("Error parsing property name")
            elif _is_property:
                if _property_name in _macro_property:
                    _macro_property[_property_name] += ProjectConfig.LINE_SEPARATOR + _vba_code
                else:
                    _macro_property[_property_name] = _vba_code
            else:
                pass
        self.__macro_property__ = _macro_property

    def __generate_function_calls(self):
        _function_calls = []
        _relation = {}
        for __function_name in self.__macro_functions__:
            if __function_name not in _function_calls:
                _function_calls.append(__function_name)
                _relation[__function_name] = ''
        # analyze function calls
        for __function_name in self.__macro_functions__:

            __function_code = self.__macro_functions__[__function_name]
            __function_tokens = list(filter(None, re.split('[\"(, \-!?:\r\n)&=.><]+', __function_code)))
            for ___function_name in self.__macro_functions__:
                # orig_func_name = func_name1
                ___function_position = ___function_name.find(" ")
                if ___function_position > -1:
                    ___function_name = ___function_name[:___function_position]

                for ____index in range(0, __function_tokens.count(___function_name)):
                    if __function_name != ___function_name:
                        if self.__check_key_combination(_relation, __function_name):
                            if ___function_name not in _relation[__function_name]:
                                _relation[__function_name].append(___function_name)
                        else:
                            ____function_name = [___function_name]
                            _relation[__function_name] = ____function_name

        return _relation

    @staticmethod
    def __check_key_combination(_function_code, _function_name):
        try:
            if _function_code[_function_name]:
                return True
        except KeyError:
            return False

    def __extract_keywords(self):
        _macro_malicious_keywords = {}
        _macro_code = self.__macro_functions__
        for __function_name in _macro_code:
            __function_keywords = []
            __function_code = _macro_code[__function_name]
            __function_vba_code = filter(None, re.split("\n", __function_code))
            __sensitive_keywords = "(" + ")|(".join(ProjectConfig.LIST_MALICIOUS_CASE_SENSITIVE) + ")"
            __in_sensitive_keywords = "(" + ")|(".join(ProjectConfig.LIST_MALICIOUS_CASE_INSENSITIVE) + ")"
            for ___code_match in __function_vba_code:
                ___keywords_matches = re.findall(__sensitive_keywords, ___code_match)
                ___keywords_in_sensitive_matches = re.findall(__in_sensitive_keywords, ___code_match, re.IGNORECASE)
                ___all_keywords = ___keywords_matches + ___keywords_in_sensitive_matches
                if ___all_keywords:
                    for _this_match in ___all_keywords:
                        __this_match_list = list(_this_match)
                        for __match_of_list in __this_match_list:
                            if '' != __match_of_list and __match_of_list not in __function_keywords:
                                __function_keywords.append(__match_of_list)
            _macro_malicious_keywords[__function_name] = __function_keywords
        return _macro_malicious_keywords

    def __call_functions(self):
        _decoded_macro = {}
        try:
            self.__remove_anomalies()
            self.__extract_function()
            self.__extract_properties()
            self.__macro_functions__.update(self.__macro_property__)
            _decoded_macro['function_calls'] = self.__generate_function_calls()
            _decoded_macro['complete_code'] = self.__macro_functions__
            _decoded_macro['keywords_macro'] = self.__extract_keywords()
            return True, _decoded_macro
        except Exception as e:
            return False, 'Failed to normalize macro function. ' + str(e)

    def get_data(self):
        return self.__call_functions()
