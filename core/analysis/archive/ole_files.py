__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from oletools.oleid import olefile


class OleFiles:

    def __init__(self, file_path=None):
        if file_path:
            self.__file_path__ = file_path

    def __ole_structure(self):
        ole = olefile.OleFileIO(self.__file_path__)
        file_list = []
        for _list in ole.listdir():
            if len(_list) > 1:
                for item in range(len(_list) - 1):
                    ole_structure = {'parent': _list[item], 'child': _list[item + 1]}
                    if ole_structure not in file_list:
                        file_list.append(ole_structure)
            else:
                ole_structure = {'parent': _list[0], 'child': None}
                if ole_structure not in file_list:
                    file_list.append(ole_structure)
        return file_list

    def get_ole_structure(self, file_path=None):
        structure_info = {'structure': {}, 'error': []}

        if file_path:
            self.__file_path__ = file_path

        try:
            if self.__file_path__:
                structure_info['structure'] = self.__ole_structure()
                sorted_list = sorted(structure_info['structure'], key=lambda k: k['parent'])
                structure_info['structure'] = sorted_list
            return structure_info
        except AttributeError:
            structure_info['error'] = 'No file path was given.'
            return structure_info
        #
