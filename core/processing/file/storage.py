__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
import random
import string
import os
import subprocess
import shutil

from config.common import BASE_DIR
from core.analysis.identification import *
from core.analysis.archive import *
from core.processing.file.create_json import CreateJson
from core.analysis.macro.extract_macro import ExtractMacro
from core.analysis.macro.code_normalization import CodeNormalization
from core.analysis.virustotal.virustotal import Virustotal
from core.analysis.cryptam.cryptam import Cryptam
from core.analysis.doc_info.document_information import DocumentInformation
from core.analysis.macro.macro_indicators import MacroIndicators
from core.analysis.embedded_objects.object_information import ObjectInformation
from core.analysis.ooxml.xml_analysis import XmlAnalysis

class Storage:
    def __init__(self, file_object, local_storage=False, object_extraction=False, modules=None):
        """
        This class is meant to storage sample and process selected modules.
        :param file_object: Sample or object passed to function for process
        :param local_storage: Boolean variable, either storage is enabled or disabled
        :param object_extraction: Boolean variable, either object extraction against give object enabled or not
        :param modules: dictionary of modules while will be executed on sample
        """
        if modules is None:
            modules = {}
        # Initialization of class level objects
        self.__file_object__ = file_object
        self.__local_storage__ = local_storage
        self.__object_extraction__ = object_extraction
        self.__modules__ = modules
        self.__temporary_location__ = None
        self.__original_name__ = None
        self.__original_extension__ = None

        self.__random_name__ = None

    # noinspection PyBroadException
    def __temporary_storage(self):
        """
        This function will call random name generation function and store file with file extension. For other processing
        modules we'll using this created file.
        :return: Function will return either True or False depending upon the successful storage of file on dictionary
        """
        try:
            random_file_name = self.__random_name_generation()
            self.__random_name__ = random_file_name
            file_name, file_extension = os.path.splitext(self.__file_object__.filename)
            self.__original_name__ = file_name

            if '.' in file_extension:
                file_extension = file_extension.replace('.', '')
                if file_extension:
                    self.__original_extension__ = file_extension
                    file_extension = "." + file_extension

            # Temporary saved location for sample to be stored.
            self.__temporary_location__ = BASE_DIR + '/' + random_file_name + file_extension

            # Storing file on disk
            self.__file_object__.save(self.__temporary_location__)
            return True
        except:
            return False

    @staticmethod
    def __random_name_generation():
        """
        This function will generate random file name for files which will be temporarily stored during processing of
        modules. This will help us to ignore the cases where same name files are copied at server side.
        help : https://stackoverflow.com/a/2257492/9014930
        :return: This function will return a string of 32 characters randomly
        """
        name_length = 32
        random_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(name_length))
        return random_name

    def __basic_information(self):
        """
        This function will provide us some basic information related to sample/object. We'll be collecting sample's real
        file name, it's real extension, size of file in bytes and normal easy readable size.
        :return: This function will return a dictionary of four keys
        {'name': 'sample2', 'extension': 'doc', 'file_size': 28608, 'file_size_readable': '27.9 KB'}
        """
        sample_information = {'name': self.__original_name__, 'extension': self.__original_extension__, 'file_size': '',
                              'file_size_readable': ''}
        file_size = FileSize(self.__temporary_location__)
        was_success, size_info = file_size.do_size_calculation()
        sample_information['file_size'] = size_info['file_size']
        sample_information['file_size_readable'] = size_info['file_size_readable']
        return sample_information

    def __identification(self):
        """
        This function is to identify some basic information related to file type of uploaded sample. We have added three
        different methods in this regard.
        - Identify : This will help us to difference between different text file types like simple text, js, ps1, cmd
        - Extension : What was the extension of given sample with file name
        - Magic value : This will provide us magic (mime) information of sample. It will also try to find file extension
        of any given file type on the bases of mime information. A list of extension on the bases of mime is added into
        py file.
        :return: function will return a dictionary which will contain output of all these modules
         {'file_type_tags': {'file', 'non-executable', 'binary'}, 'file_extension': 'doc', 'magic':
         {'mime': 'application/msword', 'mime_extension': 'doc'}
        """
        file_identification = {'file_type_tags': {}, 'file_extension': '', 'magic': {}}
        # Identify file tags
        """
        This will help us to identify different text file formats e.g. simple text, javascript, php, html etc ..
        """
        file_identify = FileIdentify(self.__temporary_location__)
        was_success, file_iden = file_identify.do_file_identify()
        if was_success and 'file_type_tags' in file_iden:
            file_identification['file_type_tags'] = file_iden['file_type_tags']

        # File extension extraction
        # This will extract extension from uploaded file
        file_extension = FileExtension(self.__temporary_location__)
        was_success, file_iden = file_extension.do_extract_extension()
        if was_success and 'file_name' in file_iden:
            file_identification['file_extension'] = file_iden['file_extension']

        # File magic information
        file_magic = FileMagic(self.__temporary_location__)
        was_success, file_iden = file_magic.do_magic_identification()
        if was_success:
            mime_info = {'mime': file_iden['mime'], 'mime_extension': file_iden['mime_file_type']}
            file_identification['magic'] = mime_info
        return file_identification

    def __hash_calculation(self):
        """
        This function will help us to collect information related to different hashes value. We'll be calculating fuzzy
        hash, md5sum, sha1sum, sha256sum in this function and then create a dictionary for the sample. These hashes will
        be used for unique identification and similarity match.
        :return: A dictionary will be returned with fuzzy_hash, md5sum, sha1sum, sha256sum following pattern will be
        returned
        {'fuzzy_hash': None, 'md5sum': None, 'sha1sum': None, 'sha256sum': None}
        """
        hash_iden = {'fuzzy_hash': None, 'md5sum': None, 'sha1sum': None, 'sha256sum': None}
        fuzzy_hash = FuzzyHash(self.__temporary_location__)
        was_success, hash_info = fuzzy_hash.do_fuzzy_calculation()
        if was_success:
            hash_iden['fuzzy_hash'] = hash_info['fuzzy_hash']

        sample_hashes = CalculateHash(self.__temporary_location__)
        was_success, hash_info = sample_hashes.do_hash_calculation()
        if was_success:
            hash_iden['md5sum'] = hash_info['md5sum']
            hash_iden['sha1sum'] = hash_info['sha1sum']
            hash_iden['sha256sum'] = hash_info['sha256sum']
        return hash_iden

    def __generate_explorer_view(self):
        """
        This function generates explorer view of embedded files. We are currently using 7z for this propose. By adding
        this we are able to look through office file type and identify templates file structure and other embedded
        resources. This function is not alternative of embedded object extraction. This will help us to view objects
        and understand structure.
        :return: In response function will generate a complete dictionary which contains information about relationship
        of files with their parents.
        """
        file_view = SevenZip(self.__temporary_location__)
        was_successful, relationship = file_view.get_structure_info()
        core = {}
        sorted_list = []
        if was_successful:
            if relationship['structure']:
                data = []
                for item in relationship['structure']:
                    if not item['child']:
                        icon = self.__font_awesome(item['parent'])
                        if icon:
                            node = {'id': item['parent'], 'parent': '#', 'text': item['parent'], "icon": icon}
                        else:
                            node = {'id': item['parent'], 'parent': '#', 'text': item['parent']}
                    else:
                        icon = self.__font_awesome(item['child'])
                        if icon:
                            node = {'id': item['child'], 'parent': item['parent'],
                                    'text': item['child'], "icon": icon}
                        else:
                            node = {'id': item['child'], 'parent': item['parent'],
                                    'text': item['child']}
                    data.append(node)
                sorted_list = sorted(data, key=lambda k: k['parent'])
        core['data'] = sorted_list
        return {'core': core}

    def __extract_macro(self):
        file_location = self.__temporary_location__
        _object_extract_macro = ExtractMacro(file_location)
        was_success, macro_code = _object_extract_macro.do_macro_extraction()
        if was_success:
            return macro_code
        else:
            return ''

    def __embedded_location(self, location):
        if not os.path.isdir(location):
            obj_info = ObjectInformation(location)
            obj_info.extract_information()
        else:
            for item in os.listdir(location):
                self.__embedded_location((location + '/' + item) if location != '/' else '/' + item)

    def __extract_file(self):
        try:
            if os.path.exists(BASE_DIR + '/' + self.__random_name__):
                self.__random_name__ = self.__random_name__ + "_" + str(1)
            cmd = ['7z', 'x', self.__temporary_location__, '-o' + BASE_DIR + '/' + self.__random_name__, '-y']
            try:
                subprocess.check_output(cmd).decode("utf-8")
                # self.__embedded_location(BASE_DIR + '/' + self.__random_name__)
                ooxml_obj = XmlAnalysis(BASE_DIR + '/' + self.__random_name__)
                ooxml_obj.xml_information()
            except AttributeError:
                return False
            except UnboundLocalError:
                return False
        except Exception as e:
            print(e)

    @staticmethod
    def __macro_code_normalization(macro_code):
        _obj = CodeNormalization(macro_code)
        was_successful, details = _obj.do_normalization()
        if was_successful:
            return details
        else:
            return {}

    @staticmethod
    def __execute_virustotal(md5sum):
        obj = Virustotal(md5sum)
        return obj.fetch_results()

    @staticmethod
    def __font_awesome(indicator):
        """
        Identified different font awesome icons for different file names supported in office documents structure. We
        have added different icons and images to quick view and issue identification.
        :param indicator: indicator or string passed to this function.
        :return: font awesome / feature icon code is returned in response.
        """
        if indicator.lower().endswith('.xml'):
            return 'fa fa-file-code-o'
        elif indicator.lower().endswith('.rels'):
            return 'fa fa-copy'
        elif indicator.lower().endswith('.bin'):
            return 'fa fa-bug'
        elif indicator.lower().endswith('.vml') or indicator.lower().endswith('.emf') or indicator.lower().endswith(
                '.png') or indicator.lower().endswith('.jpg') or indicator.lower().endswith(
            '.jpeg') or indicator.lower().endswith('pictures') or indicator.lower().endswith(
            'wmf') or indicator.lower().endswith('gif') or indicator.lower().endswith('wdp'):
            return 'fe fe-image'
        elif indicator.lower().endswith('table'):
            return 'fa fa-table'
        elif indicator.lower().endswith('worddocument'):
            return 'fa fa-file-word-o'
        elif indicator.lower().endswith('powerpoint document'):
            return 'fa fa-file-powerpoint-o'
        elif indicator.lower().endswith('Workbook') or indicator.lower().endswith('xls') or indicator.lower().endswith(
                'xlsx'):
            return 'fa fa-file-excel-o'
        elif indicator.lower().endswith('compobj'):
            return 'fe fe-settings'
        elif indicator.lower().endswith('summaryinformation'):
            return 'fa fa-list-alt'
        elif indicator.lower().endswith('data'):
            return 'fa fa-group'
        elif indicator.lower().endswith('todole'):
            # http://moosewoler.github.io/%E7%8E%A9%E6%84%8F%E5%84%BF/2014/11/18/%E5%A6%82%E4%BD%95%E5%88%A0%E9%99%A4toDOLE%E5%AE%8F%E7%97%85%E6%AF%92.html
            return 'fa fa-bomb'
        elif indicator.lower().endswith('current user'):
            return 'fe fe-user'
        elif indicator.endswith('Ole'):
            return 'fa fa-bomb'
        elif 'Ole' in indicator or indicator.lower().endswith('exe'):
            return 'fa fa-bomb'
        elif 'Ole' in indicator and 'Native' in indicator:
            return 'fa fa-bomb'
        elif 'ObjectPool' in indicator:
            return 'fa fa-bug'
        elif 'ThisDocument' in indicator:
            return 'fe fe-file'
        elif 'startup' in indicator.lower():
            return 'fa fa-windows'
        elif '__SRP_' in indicator:
            # https://msdn.microsoft.com/en-us/library/dd944619(v=office.12).aspx
            return 'fa fa-pencil-square-o'
        elif 'Sheet' in indicator or 'Workbook' in indicator:
            return 'fa fa-file-excel-o'
        elif 'dir' == indicator:
            return 'fe fe-folder'
        elif '_VBA_PROJECT' in indicator or 'PROJECT' in indicator:
            return 'fe fe-code'

    @staticmethod
    def __get_cryptam_information(sha256sum):
        obj = Cryptam(sha256sum=sha256sum)
        return obj.fetch_results()

    def __get_doc_information(self):
        try:
            obj = DocumentInformation(self.__temporary_location__)
            return obj.extract_doc_attributes()
        except OSError:
            return {}

    @staticmethod
    def __get_macro_indicators(macro_code):
        obj = MacroIndicators(macro_code=macro_code)
        return obj.get_macro_ioc()

    def __process_modules(self):
        """
        This function will act like a bridge to call child functions and collect their returned data. Later this data
        will be made a part of dictionary and returned to it's caller
        :return: A dictionary will be returned with complete information of modules and details
        """
        macro_code = self.__extract_macro()
        results = {'basic_info': self.__basic_information(), 'file_type': self.__identification(),
                   'hashes': self.__hash_calculation(), 'explorer_view': self.__generate_explorer_view(),
                   'macro_code': macro_code, 'graph_data': self.__macro_code_normalization(macro_code),
                   'doc_summary': self.__get_doc_information()
                   }
        self.__extract_file()

        if not self.__local_storage__:
            os.remove(self.__temporary_location__)
        if os.path.isdir(BASE_DIR + '/' + self.__random_name__):
            shutil.rmtree(BASE_DIR + '/' + self.__random_name__)
        if macro_code:
            results['macro_code_ioc'] = self.__get_macro_indicators(macro_code)

        results['virustotal'] = self.__execute_virustotal(results['hashes']['md5sum'])
        results['cryptam'] = self.__get_cryptam_information(results['hashes']['sha256sum'])

        create_json = CreateJson(results['hashes']['md5sum'], results)

        create_json.create_json()
        try:
            return True, results['hashes']['md5sum']
        except:
            return False,

    def process_file(self):
        results = {}
        if not self.__temporary_storage():
            results['status'] = False
            results['return_value'] = 'Unable to process files, failed to store file in given location. Kindly check' \
                                      ' if correct configuration was provided.'
            return results
        if not self.__modules__:
            return_code, return_value = self.__process_modules()
            results['status'] = return_code
            results['return_value'] = return_value
            return results
