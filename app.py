__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from flask import Flask

from view.ui import index_page
from view.ui import analysis_report
from view.ui import project_settings

from view.ajax.upload_samples import ajax_sample_upload
from view.ajax.load_reports import ajax_reports
from view.ajax.update_config import ajax_update_config

app = Flask(__name__)

# Url
app.register_blueprint(index_page)
app.register_blueprint(analysis_report)
app.register_blueprint(project_settings)

# Ajax Calls
app.register_blueprint(ajax_sample_upload)
app.register_blueprint(ajax_reports)
app.register_blueprint(ajax_update_config)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
