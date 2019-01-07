__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from oletools.olevba3 import *


class ExtractMacro:
    """
    This class uses oletool's VBA Parser to extract macro from ole document. We'll use this extracted macro for
    graph processing & different modules to generate verdict on given file.
    """

    def __init__(self, _file_path=None):
        """
        This is init function of extract macro. We'll initialize different variable and function in this function.

        :param _file_path: This parameter is physical path of file on which we'll perform our macro extraction.
        """
        if _file_path:
            self.__file_path__ = _file_path

    def do_macro_extraction(self, _file_path=None):
        """
        This function will use oletool's VBA parser and try extract macro code from given file.

        :param _file_path: This parameter is physical path of file on which we'll perform our macro extraction.
        :return: Function will return a tuple (boolean, string), Detail of returned value as follow
        In case of success,
        True, 'macro code extracted from document.'
        False, 'string will contain information either it's a exception or document doesn't contain any macro'
        """
        if _file_path:
            self.__file_path__ = _file_path

        _vba_code = ''  # Variable to hold complete macro code through streams
        _vba_project_bin = ''  # Variable to handle project bin file after parsing
        try:
            _vba_project_bin = VBA_Parser(self.__file_path__)
        except FileNotFoundError:
            _vba_project_bin.close()
            # Exception handling for file not found.
            return False, 'No such file or directory. Please select correct path.'
        except FileOpenError as e:
            if 'need to run rtfobj.py' in str(e):
                pass
            return False, 'Not supported'

        # Looping throw the values of parsed macro code.
        for (__child_file, __child_stream_path, __vba_file, __vba_code) in _vba_project_bin.extract_macros():
            try:
                _vba_code = _vba_code + __vba_code.decode('latin-1')
            except AttributeError:
                _vba_project_bin.close()

                # Exception handling if decoding is not applied as expected or file doesn't contain macro
                return False, 'Unable to perform macro extraction. Please ensure you are using correct file for ' \
                              'macro extraction.'

        if not _vba_code:
            _vba_project_bin.close()

            # If code variable is empty, it mean document doesn't contain any macro.
            return False, "Document doesn't contain any macro"
        _vba_project_bin.close()

        # Successfully extracted macro code from document.
        return True, _vba_code
