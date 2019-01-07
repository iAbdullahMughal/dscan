__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
import os
import ntpath


class FileExtension:

    def __init__(self, file_path=None):
        if file_path:
            self.__file_path__ = file_path

    def __get_file_extension(self):
        file_name, file_extension = os.path.splitext(self.__file_path__)
        if '.' in file_extension:
            file_extension = file_extension.replace('.', '')
        return file_name, file_extension

    def __get_file_name(self):
        head, tail = ntpath.split(self.__file_path__)
        return tail or ntpath.basename(head)

    def do_extract_extension(self, file_path=None):
        file_info = {'file_name': '', 'file_extension': '', 'error': ''}
        if file_path:
            self.__file_path__ = file_path
        if not self.__file_path__:
            file_info['error'] = 'No file path was given.'
            
        location, file_extension = self.__get_file_extension()
        file_info['file_extension'] = file_extension

        file_info['file_name'] = self.__get_file_name()

        return True, file_info
