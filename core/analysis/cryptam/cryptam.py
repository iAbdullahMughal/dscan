__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

import requests


class Cryptam:

    def __init__(self, sha256sum):
        self.__url__ = "https://cdn.cryptam.com/reports/" + sha256sum + ".json"

    def fetch_results(self):
        """
        This function will get results from cryptam website by using url get request. In this function we are not
        uploading or sharing any file with the website. This function will send a request on cryptam website by
        appending sha256sum of sample with the file. After request is successfully done, we'll collect response and
        dump into our json file for analysis.
        :return: dictionary will be returned. It's template will be as following.
        {
          "completed": true,
          "content-type": "Microsoft Word 2007+",
          "embedded_objects": [
            {
              "cryptam": "",
              "md5sum": "",
              "cryptam_id": "",
              "object_name": "",
              "object_embedded_in": "",
              "sha1sum": "",
              "sha256sum": "",
              "ssdeep": ""
            }
          ],
          "filename": "",
          "filesize": "",
          "has_embed": true,
          "has_exe": true,
          "is_malware": true,
          "summary": [
            {
              "content_id": "",
              "content_description": ""
            }
          ],
          "file_name": ""
        }
        """
        results = {}
        try:
            cryptam_report = requests.get(url=self.__url__)
            response = cryptam_report.json()
        except Exception as e:
            return results

        if 'completed' in response:
            if response['completed']:
                results['completed'] = True
            else:
                results['completed'] = False
        if 'content-type' in response:
            if response['content-type']:
                results['content-type'] = response['content-type']
        embedded_object_list = []
        if 'drop_files' in response:
            if response['drop_files']:
                counter = 0
                embedded_objects = {}
                for file_info in response['drop_files'].split("="):
                    if not '\n' in file_info:
                        if counter == 0:
                            embedded_objects['cryptam'] = file_info
                        elif counter == 1:
                            embedded_objects['md5sum'] = file_info
                        elif counter == 2:
                            embedded_objects['cryptam_id'] = file_info
                        elif counter == 3:
                            embedded_objects['object_name'] = file_info
                        elif counter == 4:
                            embedded_objects['object_embedded_in'] = file_info
                        elif counter == 5:
                            embedded_objects['sha1sum'] = file_info
                        elif counter == 6:
                            embedded_objects['sha256sum'] = file_info
                        elif counter == 7:
                            embedded_objects['ssdeep'] = file_info
                            embedded_object_list.append(embedded_objects)
                            embedded_objects = {}
                            counter = 0
                        counter += 1
        results['embedded_objects'] = embedded_object_list
        if 'detection_engine' in response:
            results['detection_engine'] = response['engine']
        if 'filename' in response:
            results['filename'] = response['filename']
        if 'filesize' in response:
            results['filesize'] = response['filesize']
        if 'has_embed' in response:
            if not response['has_embed'] == '0':
                results['has_embed'] = True
            else:
                results['has_embed'] = False
        if 'has_exe' in response:
            if not response['has_exe'] == '0':
                results['has_exe'] = True
            else:
                results['has_exe'] = False
        if 'is_malware' in response:
            if response['is_malware']:
                results['is_malware'] = True
            else:
                results['is_malware'] = False
        if 'summary' in response:
            summary = response['summary'].split('\n')
            triggered_rules = []
            for summary_content in summary:
                if len(summary_content.split(':')) == 2:
                    content_id, content_description = summary_content.split(':')
                    content_type, content_description = content_description.split(".", 1)
                    rules = {'content_id': content_id, 'content_type': content_type,
                             'content_description': content_description}
                    triggered_rules.append(rules)
            results['summary'] = triggered_rules
        if 'origfilename' in response:
            results['file_name'] = response['origfilename']
        return results
