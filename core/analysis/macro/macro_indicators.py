__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from oletools.olevba3 import *


class MacroIndicators:

    def __init__(self, macro_code):
        """
        Init function
        :param macro_code: extracted macro code from document, we'll be using this code for macro code analysis by
        using olevba3 tool.
        """
        self.__macro_code__ = macro_code

    def __extract_information(self):
        """
        This function will extract iocs information from macro code using olevba3 library. Via this method we'll
        covering following areas;
        1. Vba Strings
        2. Suspicious Strings
        3. Auto executable functions
        4. Base64 encoded strings
        5. Dridex strings
        6. Hex encoded strings
        :return: This function will return a dictionary of these values
        """
        iocs_macro_code = {}
        counter = 0
        vba_strings = []
        for element in detect_vba_strings(self.__macro_code__):
            node_value = {'key': element[0], 'value': element[1].replace('(use option --deobf to deobfuscate)', '')}
            vba_strings.append(node_value)
            counter += 1
        iocs_macro_code['vba_strings'] = vba_strings
        iocs_macro_code['vba_strings_counter'] = counter

        counter = 0
        suspicious = []
        for element in detect_suspicious(self.__macro_code__):
            node_value = {'key': element[0], 'value': element[1].replace('(use option --deobf to deobfuscate)', '')}
            suspicious.append(node_value)
            counter += 1
        iocs_macro_code['suspicious'] = suspicious
        iocs_macro_code['suspicious_counter'] = counter

        counter = 0
        autoexec = []
        for element in detect_autoexec(self.__macro_code__):
            node_value = {'key': element[0], 'value': element[1].replace('(use option --deobf to deobfuscate)', '')}
            autoexec.append(node_value)
            counter += 1
        iocs_macro_code['autoexec'] = autoexec
        iocs_macro_code['autoexec_counter'] = autoexec

        counter = 0
        base64_strings = []
        for element in detect_base64_strings(self.__macro_code__):
            node_value = {'key': element[0], 'value': element[1].replace('(use option --deobf to deobfuscate)', '')}
            base64_strings.append(node_value)
            counter += 1
        iocs_macro_code['base64_strings'] = base64_strings
        iocs_macro_code['base64_strings_counter'] = counter

        counter = 0
        dridex_strings = []
        for element in detect_dridex_strings(self.__macro_code__):
            node_value = {'key': element[0], 'value': element[1].replace('(use option --deobf to deobfuscate)', '')}
            dridex_strings.append(node_value)
            counter += 1
        iocs_macro_code['dridex_strings'] = dridex_strings
        iocs_macro_code['dridex_strings_counter'] = counter

        counter = 0
        hex_strings = []
        for element in detect_hex_strings(self.__macro_code__):
            node_value = {'key': element[0], 'value': element[1].replace('(use option --deobf to deobfuscate)','')}
            hex_strings.append(node_value)
            counter += 1
        iocs_macro_code['hex_strings'] = hex_strings
        iocs_macro_code['hex_strings_counter'] = counter

        counter = 0
        patterns = []

        for element in detect_patterns(self.__macro_code__):
            node_value = {'key': element[0], 'value': element[1].replace('(use option --deobf to deobfuscate)', '')}
            patterns.append(node_value)
            counter += 1
        iocs_macro_code['patterns'] = patterns
        iocs_macro_code['patterns_counter'] = counter

        return iocs_macro_code

    def get_macro_ioc(self):
        return self.__extract_information()
