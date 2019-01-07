__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
import os


class FileSize:

    def __init__(self, file_path):
        self.__file_path__ = file_path

    # https://stackoverflow.com/questions/2104080/how-to-check-file-size-in-python
    @staticmethod
    def __convert_bytes(number_value):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if number_value < 1024.0:
                return "%3.1f %s" % (number_value, x)
            number_value /= 1024.0

    def __file_size(self):
        """
        this function will return the file size
        """
        file_size = {'file_size': None, 'file_size_readable': None, 'error': []}
        try:
            file_info = os.stat(self.__file_path__)
            file_size['file_size'] = file_info.st_size
            file_size['file_size_readable'] = self.__convert_bytes(file_info.st_size)
            return True, file_size
        except FileNotFoundError:
            file_size['error'].append('No file path was given.')
            return False, file_size

    def do_size_calculation(self, file_path=None):
        file_size = {'file_size': None, 'file_size_readable': None, 'error': []}
        if file_path:
            self.__file_path__ = file_path

        if not self.__file_path__:
            file_size['error'].append('No file path was given.')
            return file_size

        was_successful, file_size = self.__file_size()
        return was_successful, file_size
