__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from config.common import BASE_DIR
import os
import json


class LoadJson:

    def __init__(self):

        self.__reports_folder__ = BASE_DIR + "/report"
        if not os.path.exists(self.__reports_folder__):
            self.__reports_folder__ = BASE_DIR

    def load_json_content(self, md5sum):
        json_content = {}
        path_to_json = self.__reports_folder__
        for file in os.listdir(path_to_json):
            full_filename = "%s/%s" % (path_to_json, file)
            if md5sum in full_filename:
                if os.path.isfile(full_filename):
                    with open(full_filename, 'r') as fi:
                        json_content = json.load(fi)

                        break
        return json_content

    def load_json_list(self):
        records = []
        path_to_json = self.__reports_folder__
        try:
            for file in os.listdir(path_to_json):
                full_filename = "%s/%s" % (path_to_json, file)
                if os.path.isfile(full_filename):
                    with open(full_filename, 'r') as fi:

                        try:
                            json_content = json.load(fi)
                            sample_information = {'sample_name': json_content['basic_info']['name'],
                                                  'md5sum': json_content['hashes']['md5sum'],
                                                  'sample_extension': json_content['basic_info']['extension'],
                                                  'sample_size': json_content['basic_info']['file_size_readable']
                                                  }
                            records.append(sample_information)
                        except KeyError:
                            pass
                        except:
                            pass
        except FileNotFoundError:
            pass

        return json.dumps({'data': records})
