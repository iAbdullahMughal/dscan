__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

import subprocess


class SevenZip:
    """
    This class will use 7z application and extract structure of file.
    """

    def __init__(self, file_path):
        self.__file_path__ = file_path

    @staticmethod
    def __normalize_structure(content):
        if len(content) == 1:
            storage_structure = {'parent': content[0], 'child': None}
            return storage_structure
        elif len(content) == 2:
            storage_structure_list = []
            storage_structure = {'parent': content[0], 'child': None}
            storage_structure_list.append(storage_structure)
            storage_structure = {'parent': content[0], 'child': content[1]}
            storage_structure_list.append(storage_structure)

            return storage_structure_list
        else:
            storage_structure_list = []
            for i in range(len(content) - 1):
                storage_structure = {'parent': content[i], 'child': content[i + 1]}
                storage_structure_list.append(storage_structure)
            return storage_structure_list

    def get_structure_info(self, file_path=None):
        structure_info = {'structure': {}, 'error': []}
        seven_zip = []
        if file_path:
            self.__file_path__ = file_path
        if not self.__file_path__:
            structure_info['error'] = 'No file path was given.'
            return False, structure_info
        try:
            cmd = ['7z', 'l', self.__file_path__, '-r-']
            try:
                seven_zip = subprocess.check_output(cmd).decode("utf-8").split('\n')
            except AttributeError:
                return False, structure_info
            except UnboundLocalError:
                return False, structure_info
            relation_list = []
            j = 0
            for line in seven_zip:
                if '------------------------' in line:
                    j += 1
                    while j < len(seven_zip):
                        # first 53 characters are information related to file it's date and size
                        # Not our usage
                        _line = seven_zip[j][53:]
                        if '------------------------' in _line:
                            break
                        file_view = _line.split('/')
                        relational_view = self.__normalize_structure(file_view)
                        if isinstance(relational_view, dict):
                            if relational_view not in relation_list:
                                relation_list.append(relational_view)
                        elif isinstance(relational_view, list):
                            for i in range(len(relational_view)):
                                if relational_view[i] not in relation_list:
                                    relation_list.append(relational_view[i])
                        j += 1
                j += 1
            structure_info['structure'] = relation_list
            sorted_list = sorted(structure_info['structure'], key=lambda k: k['parent'])
            structure_info['structure'] = sorted_list
        except subprocess.CalledProcessError as e:
            structure_info['error'] = e
            return False, structure_info
        return True, structure_info
