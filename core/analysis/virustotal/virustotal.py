__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from virus_total_apis import PublicApi as VirusTotalPublicApi
from core.processing.config_parsing.configuration import Configuration


class Virustotal:

    def __init__(self, md5sum):
        self.__md5sum__ = md5sum
        self.__api_key__ = ""

    def fetch_results(self):
        obj = Configuration()
        return_type, api_key = obj.get_virustotal_apikey()
        if not return_type:
            return []
        else:
            self.__api_key__ = api_key
        vt = VirusTotalPublicApi(self.__api_key__)
        response = vt.get_file_report(self.__md5sum__)
        vt_results = {}
        results = []
        try:
            if response["response_code"] == 200:
                # results.append({'total': response['results']['total']})
                for av_name in response['results']['scans']:
                    av_detection = {'av_name': av_name, 'detected': response['results']['scans'][av_name]['detected'],
                                    'version': response['results']['scans'][av_name]['version'],
                                    'result': response['results']['scans'][av_name]['result']}
                    results.append(av_detection)
                vt_results['total_detection'] = response['results']['positives']
                vt_results['detection_info'] = results
                return vt_results
        except KeyError:
            pass
        return vt_results
