__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
from mmbot import MaliciousMacroBot


class MMbot:

    def __init__(self):
        pass

    def get_results(self, sample_path):
        mmb = MaliciousMacroBot()
        mmb.mmb_init_model()
        result = mmb.mmb_predict(sample_path)
        print(result.iloc)


obj = MMbot()
obj.get_results('/home/joker/Desktop/test_samples/014760.docx')
