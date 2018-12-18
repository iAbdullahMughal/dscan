__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
from config.config import LocationConfig as config
from oletools.olevba3 import *


class GenerateGraph:
    """
    This class will generating UI data for given sample. We'll read through json file and read content. These content
    will be used for creating marmaid.js input as well as javascript code for dialog module.
    We are also handling sample details and its information by using this class. Data will be populated into
    dictionary and passed to it's caller.
    """

    def get_cords(self, json_file):
        """
        This function load data from json file and parse this data for creating dictionary. This dictionary contains
        all related information for web UI page.
        :param json_file: file location of json file
        :return: Tuple will be returned to caller First boolean / second dictionary
        boolean will be result of operation while second parameter will contain information related to sample.
        """
        function_calls = ''  # Function level variable to handle all function calls and custom strings for marmaid.js
        ui_javascript = ''  # This variable holds data related to vba and javascript code which will be displayed

        sample_information = {} # A dictionary which will contains some basic information about sample
        try:
            """
            Loading json related to md5sum
            """
            with open(config.JSON_LOCATION + json_file) as json_data:
                container = json.load(json_data)
                # Calling function to extract basic information related to sample and extracting some known information
                # from vba macro code
                sample_information = self.__load_sample_information(container)

                try:
                    for function_name in container['function_calls']:
                        for child_function in container['function_calls'][function_name]:
                            function_keywords = ''
                            style = ''
                            if child_function in container['keywords_macro']:
                                for suspicious_call in container['keywords_macro'][child_function]:

                                    try:
                                        if 'shell' in suspicious_call.lower() and self.__not_me('shell',
                                                                                                function_keywords):
                                            function_keywords = function_keywords + '<br/>' + 'fa:fa-bomb Shell Activity'
                                            style = 'style ' + child_function + ' fill:#20a8d8'
                                        elif 'process' in suspicious_call.lower() and self.__not_me('process',
                                                                                                    function_keywords):
                                            function_keywords = function_keywords + '<br>' + 'fa:fa-windows Process Activity'
                                            style = 'style ' + child_function + ' fill:#ffc107'

                                        elif 'window' in suspicious_call.lower() and self.__not_me('window',
                                                                                                   function_keywords):
                                            function_keywords = function_keywords + \
                                                                '<br>' + 'fa:fa-window-maximize Tweaking Windows'
                                        elif 'download' in suspicious_call.lower() and self.__not_me('download',
                                                                                                     function_keywords):
                                            function_keywords = function_keywords + '<br>' + \
                                                                'fa:fa-cloud-download-alt Downloading Something'
                                        elif 'file' in suspicious_call.lower() and self.__not_me('file',
                                                                                                 function_keywords):
                                            function_keywords = function_keywords + '<br>' + 'fa:fa-file File Operation'
                                        elif 'application' in suspicious_call.lower() and self.__not_me(
                                                'application',
                                                function_keywords):
                                            function_keywords = function_keywords + '<br>' + 'fa:fa-magic Application Settings'
                                    except:
                                        pass
                                function_calls = function_calls + function_name + '[<b><center>' + function_name + \
                                                 '</center> </b>]' + ' --> ' + child_function + '[<b><center>' \
                                                 + child_function + '</center> </b>' + function_keywords + ']' + "\n" + style + '\n'

                    if '' == function_calls:
                        for function_name in container['function_calls']:
                            function_calls = function_calls + function_name + '[<b><center>' + function_name + \
                                             '</center> </b>]\n'

                    for function_name in container['complete_code']:
                        if '(' in function_name:
                            pass
                        else:
                            function_calls = function_calls + 'click ' + function_name + ' ' + function_name + ' ' + \
                                             '"Click for details "' + "\n"
                            ui_javascript = ui_javascript + 'var ' + function_name + \
                                            ' = function(){ document.getElementById("code").innerHTML = "' + self.__escape(
                                (container['complete_code'][function_name]).replace('\n',
                                                                                    '\\n')) + \
                                            '";$("#ex1").modal({ closeExisting: false}) }' + '\n'

                except:
                    pass
                    function_calls = ''
                    ui_javascript = ''

        except FileNotFoundError:
            pass
        ui_data = {'function_calls': function_calls, 'javascript_code': ui_javascript,
                   'sample_info': sample_information}
        return ui_data

    @staticmethod
    def __not_me(keyword, ful_string):
        if keyword.lower() not in ful_string.lower():
            return True
        else:
            return False

    @staticmethod
    def __escape(macro_code):
        return macro_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"',
                                                                                                  '&quot;').replace(
            "'", '&#39;')

    @staticmethod
    def __load_sample_information(json_content):
        """
        This is static function which reads json content and extract data from json. This data is passed to dictionary
        for proper handling.
        :param json_content: json content from json file
        :return: a dictionary is returned in response containing information related to sample.
        """
        # Fetching data from json content
        sample_information = {'file_name': json_content['file_name'], 'file_extension': json_content['file_extension'],
                              'md5sum': json_content['md5sum'], 'magic': json_content['magic'],
                              'extension': json_content['extension'], 'has_macro': json_content['has_macro']}

        """
        Following code is extracting macro code for some processing. In this processing we'll extract known data 
        from macro strings.
        """
        if 'extracted_macro' in json_content:
            sample_information['extracted_macro'] = json_content['extracted_macro']
            _detect_exe = []
            counter = 0
            for record in detect_autoexec(sample_information['extracted_macro']):
                _auto_execute = {'key': record[0], 'value': record[1]}
                _detect_exe.append(_auto_execute)
                counter = counter + 1
            sample_information['autoexe'] = _detect_exe
            sample_information['autoexe_counter'] = counter

            counter = 0
            l_base64 = []
            for record in detect_base64_strings(sample_information['extracted_macro']):
                _base64 = {'key': record[0], 'value': record[1]}
                l_base64.append(_base64)
                counter = counter + 1
            sample_information['base64'] = l_base64
            sample_information['base64_counter'] = counter

            counter = 0
            l_dridex = []
            for record in detect_dridex_strings(sample_information['extracted_macro']):
                _dridex = {'key': record[0], 'value': record[1]}
                counter = counter + 1
                l_dridex.append(_dridex)
            sample_information['dridex'] = l_dridex
            sample_information['dridex_counter'] = counter

            counter = 0
            l_hex = []
            for hex in detect_hex_strings(sample_information['extracted_macro']):
                _hex = {'key': hex[0], 'value': hex[1]}
                counter = counter + 1
                l_hex.append(_hex)
            sample_information['hex_string'] = l_hex
            sample_information['hex_string_counter'] = counter

            counter = 0
            l_patterns = []
            for record in detect_patterns(sample_information['extracted_macro']):
                _patterns = {'key': record[0], 'value': record[1]}
                counter = counter + 1
                l_patterns.append(_patterns)
            sample_information['patterns'] = l_patterns
            sample_information['patterns_counter'] = counter

            counter = 0
            l_suspicious = []
            for record in detect_suspicious(sample_information['extracted_macro']):
                _suspicious = {'key': record[0], 'value': record[1].replace(' (use option --deobf to deobfuscate)', '')}
                counter = counter + 1
                l_suspicious.append(_suspicious)
            sample_information['suspicious'] = l_suspicious
            sample_information['suspicious_counter'] = counter

        return sample_information
