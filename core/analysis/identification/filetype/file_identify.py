__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
from identify import identify


class FileIdentify:

    def __init__(self, file_path=None):
        """
        Initializing function with file path
        :param file_path: file path location
        """
        if file_path:
            self.__file_path__ = file_path

    def __identify_tags(self):
        """
        This function will identify file type tags from file content. It will help us to identify txt file types. Like
        py, js, html, power shell etc.
        :return: It will return tuple boolean and dictionary or string depending upon return type.
        """
        try:
            file_type_tags = identify.tags_from_path(self.__file_path__)
            return True, file_type_tags
        except ValueError:
            return False, 'No such file or directory.'

    def do_file_identify(self, file_path=None):
        """
        This function will check if mime definition is defined in our mime mapped file type dictionary.
        :param file_path: mime type identified by magic library
        :return: A tuple will be returned to it's caller. It's first argument will be boolean to tell either function
        was successfully executed or not while second will be dictionary with will be mime, mime_file_type and error
        list.
        """
        identify_info = {'file_type_tags': {}, 'error': []}
        if file_path:
            self.__file_path__ = file_path
        if not self.__file_path__:
            identify_info['error'] = 'No file path was given.'
            return identify_info

        was_successful, tags = self.__identify_tags()
        if was_successful:
            identified_types = []
            for tag in tags:
                identified_types.append(tag)
            identify_info['file_type_tags'] = identified_types
        else:
            identify_info['error'].append(tags)
        return True, identify_info
