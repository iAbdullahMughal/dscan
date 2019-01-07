__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
import os
from config.common import BASE_DIR
import json


class CreateJson:

    def __init__(self, file_name, json_content, folder_name="report"):
        """
        In this init function, we are providing class with some basic information which will be used to generate a json
        record for our sample. We are passing file name for json file, content of json file and folder where this report
        will be placed.
        This report will contain all required information for this project and it's view.
        :param file_name: file name of json
        :param json_content:content for json file
        :param folder_name:folder where json files will be located and saved
        """

        self.__file_name__ = file_name
        self.__json_content__ = json_content
        if folder_name:
            if self.__create_folder(folder_name):
                self.__folder_name__ = BASE_DIR + '/' + folder_name
            else:
                self.__folder_name__ = BASE_DIR

    @staticmethod
    def __create_folder(folder_name):
        try:
            folder_location = BASE_DIR + '/' + folder_name
            if not os.path.exists(folder_location):
                os.mkdir(folder_location)
            return True
        except Exception as e:
            print(e)
            return False

    def create_json(self):
        try:
            with open(self.__folder_name__ + "/" + self.__file_name__ + ".json", 'w') as json_file:
                json.dump(self.__json_content__, json_file)
            return True
        except Exception as e:
            return False
