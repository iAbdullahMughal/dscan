__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

import olefile


class DocumentInformation:
    __SUMMARY_ATTRIB = {'codepage': 'Document code page', 'title': 'Document title', 'subject': 'Document Subject',
                        'author': 'Author Name', 'keywords': 'Keywords', 'comments': 'Comments',
                        'template': 'Document Template', 'last_saved_by': 'Document last saved by',
                        'revision_number': 'Document revision version', 'total_edit_time': 'Total number of edits',
                        'last_printed': 'Last printed info', 'create_time': 'Document create time',
                        'last_saved_time': 'Document last saved time', 'num_pages': 'Total number of pages',
                        'num_words': 'Total number of words', 'num_chars': 'Total number of charts',
                        'thumbnail': 'Document thumbnail', 'creating_application': 'Document created by ',
                        'security': 'Document security information'}

    _DOCSUM_ATTRIBS = {'codepage_doc': 'Document code page', 'category': 'Document Category',
                       'presentation_target': 'Document Presentation Target', 'bytes': 'Total bytes ',
                       'lines': 'Total number of lines ', 'paragraphs': 'Total number of paragraphs',
                       'slides': 'Total number of slides', 'notes': 'Document notes', 'hidden_slides': 'Hidden slides',
                       'mm_clips': 'Media clips',
                       'scale_crop': 'Scale crop ', 'heading_pairs': 'Heading pairs ',
                       'titles_of_parts': 'Document titles',
                       'manager': 'Document Manager',
                       'company': 'Company', 'links_dirty': 'Links ', 'chars_with_spaces': 'Chars with spaces ',
                       'unused': 'Unused ', 'shared_doc': 'Shared document',
                       'link_base': 'Link base', 'hlinks': 'Hyper links ', 'hlinks_changed': 'Hyper links changed',
                       'version': 'Document version', 'dig_sig': 'Document digital Signature',
                       'content_type': 'Content type', 'content_status': 'Content Status', 'language': 'Language ',
                       'doc_version': 'Document Version'}

    def __init__(self, file_path):
        self.__ole__ = olefile.OleFileIO(file_path)

    def __extract_prop(self):
        ole_information = []
        try:

            meta = self.__ole__.get_metadata()
            for prop in self.__SUMMARY_ATTRIB:
                if meta.__getattribute__(prop):
                    _property_content = {}
                    _property_value = meta.__getattribute__(prop)
                    if isinstance(_property_value, bytes):
                        try:
                            _property_value = _property_value.decode("utf-8")
                        except:
                            pass
                    _property_content['key'] = self.__SUMMARY_ATTRIB[prop]
                    _property_content['value'] = str(_property_value)
                    ole_information.append(_property_content)

            for prop in self._DOCSUM_ATTRIBS:
                if meta.__getattribute__(prop):
                    _property_content = {}
                    _property_value = meta.__getattribute__(prop)
                    if isinstance(_property_value, bytes):
                        _property_value = _property_value.decode("utf-8")
                    _property_content['key'] = self._DOCSUM_ATTRIBS[prop]
                    _property_content['value'] = str(_property_value)
                    ole_information.append(_property_content)
        except Exception as e :
            print(e)
            pass
        return ole_information

    def extract_doc_attributes(self):
        ole_information = {'meta': self.__extract_prop()}
        return ole_information
