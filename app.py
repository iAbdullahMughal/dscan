__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

import os
from flask import (Flask,
                   request,
                   jsonify,
                   render_template,
                   Markup
                   )

from config.config import LocationConfig
from core.processing.file.process_file import ProcessFile
from core.processing.graph.generate_graph import GenerateGraph
from core.processing.file.load_project import LoadProject

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('pages/index.html')


@app.route('/sample_upload', methods=['GET', 'POST'])
def sample_upload():
    return render_template('pages/upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if not os.path.isdir(LocationConfig.JSON_LOCATION):
            os.mkdir(LocationConfig.JSON_LOCATION)
        filename = LocationConfig.JSON_LOCATION + str(file.filename)
        file.save(filename)
        try:
            obj = ProcessFile(filename)
            _return_code, _return_value = obj.process_file()
            os.remove(filename)
            upload_information = {'return_code': _return_code, 'return_value': _return_value}
        except Exception as e:
            os.remove(filename)
            upload_information = {'return_code': False, 'return_value': str(e)}
        return jsonify(upload_information)


@app.route('/load_data',methods=['GET', 'POST'])
def load_data():
    obj = LoadProject()
    return obj.load_information()


@app.route('/process', methods=['GET', 'POST'])
def process():
    sample_name = request.args.get('sample')
    obj_data = GenerateGraph()
    ui_data = obj_data.get_cords(sample_name)
    ui_javascript = ui_data['javascript_code']
    sample_info = ui_data['sample_info']
    ui_javascript = Markup(ui_javascript)
    return render_template('pages/process.html', ui_data=ui_data, ui_javascript=ui_javascript, sample_info=sample_info)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404


if __name__ == '__main__':
    app.run()
