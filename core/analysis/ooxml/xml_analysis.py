__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
import os
import xml.etree.ElementTree as ET


class XmlAnalysis:

    def __init__(self, extracted_folder):
        self.__path__ = extracted_folder

    def xml_information(self):
        for path, sub_dirs, files in os.walk(self.__path__):
            for name in files:
                if not name.endswith('.xml'):
                    continue
                xml_path = os.path.join(path, name)
                tree = ET.parse(xml_path)
                root = tree.getroot()
                print('\n\n')
                print(xml_path)
                for child in root:
                    print(child.tag, child.attrib)
