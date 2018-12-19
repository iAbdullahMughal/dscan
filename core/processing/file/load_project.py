__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
from config.config import LocationConfig
import json
import os


class LoadProject:

    def __init__(self):
        pass

    @staticmethod
    def load_information():
        json_data = []
        if not os.path.isdir(LocationConfig.JSON_LOCATION):
            os.mkdir(LocationConfig.JSON_LOCATION)
        path_to_json = LocationConfig.JSON_LOCATION
        for file in os.listdir(path_to_json):
            full_filename = "%s/%s" % (path_to_json, file)
            with open(full_filename, 'r') as fi:
                __json_content = json.load(fi)
                _sample_information = {'file_extension': __json_content['file_extension'],
                                       'file_name': __json_content['file_name'], 'magic': __json_content['magic'],
                                       'extension': __json_content['extension'], 'md5sum': __json_content['md5sum'],
                                       'has_macro': __json_content['has_macro']}
                json_data.append(_sample_information)
        return json.dumps({'data': json_data})
