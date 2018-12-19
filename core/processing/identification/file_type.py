__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
import magic


class FileType:
    """
    This class is used to identify file extension on the bases of magic value. Currently we have limited definition of
    file type mainly supported for office file types.
    """
    def __init__(self, _file_path):
        """
        Init file path from input
        :param _file_path: path of file
        """
        self.__file_path__ = _file_path

    def get_magic_value(self):
        """
        Function is identifying magic value of given file type.
        :return: tuple
            success
                boolean, dictionary
            failure
                boolean, string
        """
        try:
            _file_information = {}
            _mime = magic.Magic(mime=True)
            _mime_type = _mime.from_file(self.__file_path__)
            _file_information['mime_info'] = _mime_type
            return True, _file_information
        except:
            return False, 'Failed to identify mime type of file.'

    @staticmethod
    def identify_file_type_mime(_mime_type):
        """
         Function is identifying possible extension of the bases of mime type
        :param _mime_type: magic value of file
        :return: list of matched extensions
        """
        _file_type = []

        _mime_collection = {'doc': "application/msword", 'dot': "application/msword",
                            'docx': "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            'dotx': "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
                            'docm': "application/vnd.ms-word.document.macroEnabled.12",
                            'dotm': "application/vnd.ms-word.template.macroEnabled.12",
                            'xls': "application/vnd.ms-excel",
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
