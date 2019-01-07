__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
import ssdeep


class FuzzyHash:

    def __init__(self, file_path):
        self.__file_path__ = file_path

    def __get_fuzzy_hash(self):
        try:
            fuzzy = ssdeep.hash_from_file(self.__file_path__)
            return True, fuzzy
        except Exception as e:
            return False, str(e)

    def do_fuzzy_calculation(self, file_path=None):
        fuzzy_info = {'fuzzy_hash': None, 'error': []}
        if file_path:
            self.__file_path__ = file_path

        if not self.__file_path__:
            fuzzy_info['error'].append('No file path was given.')
            return False, fuzzy_info
        was_successful, fuzzy_hash = self.__get_fuzzy_hash()
        if was_successful:
            fuzzy_info['fuzzy_hash'] = fuzzy_hash
        else:
            fuzzy_info['error'].append(fuzzy_hash)
        if fuzzy_info['error']:
            return False, fuzzy_info
        return True, fuzzy_info
