__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'
from flask import Flask
from view.ui.main import index_page
from view.ui.analysis_report import  analysis_report

from view.ajax.upload_samples import ajax_sample_upload
from view.ajax.load_reports import ajax_reports

app = Flask(__name__)

# Url
app.register_blueprint(index_page)
app.register_blueprint(analysis_report)

# Ajax Calls
app.register_blueprint(ajax_sample_upload)
app.register_blueprint(ajax_reports)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
