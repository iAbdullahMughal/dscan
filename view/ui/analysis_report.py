__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from core.processing.file.load_json import LoadJson

analysis_report = Blueprint('analysis_report', __name__, template_folder='templates')


@analysis_report.route('/analysis_report', defaults={'page': 'index'})
@analysis_report.route('/analysis_report')
def show():
    try:
        sample_name = request.args.get('sample')
        json_object = LoadJson()
        json_content = json_object.load_json_content(sample_name)
        return render_template('pages/analysis_report.html', ui_data=None, json_content=json_content)
    except TemplateNotFound:
        abort(404)
