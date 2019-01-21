__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
from config.common import CONFIG_FILE
import configparser


class Configuration:
    def __init__(self):
        self.__config__ = configparser.ConfigParser()
        self.__config__.read(CONFIG_FILE)

    def get_virustotal_apikey(self):
        try:
            return True, self.__config__['DEFAULT']['virustotal_api_key'].strip('"')
        except Exception as e:
            return False, str(e)

    def update_virustotal_apikey(self, api_key):
        try:
            self.__config__['DEFAULT']['virustotal_api_key'] = api_key

            with open(CONFIG_FILE, 'w') as configfile:
                self.__config__.write(configfile)
                return True, 'Stored Data'

        except Exception as e:
            return False, 'Failed To Save' + str(e)
