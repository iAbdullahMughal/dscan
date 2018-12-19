__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

import os
import ntpath


class FileName:
    """
    This class is used to extract file name and extension through file name.
    """
    def __init__(self, _file_path):
        """

        :param _file_path: path of file
        """
        self.__file_path__ = _file_path

    def extract_file_name_extension(self):
        """
        This function is to identify sample name and it's extension on the bases of submission.
        :return:
        """
        try:
            _base_name, _file_extension = os.path.splitext(self.__file_path__)
            _file_name = ntpath.basename(self.__file_path__)
            _file_information = {'file_name': _file_name, 'file_extension': _file_extension}
            return True, _file_information
        except:
            return False, 'Failed to identify file type.'
