__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

project_settings = Blueprint('project_settings', __name__, template_folder='templates')


@project_settings.route('/Settings', defaults={'page': 'index'})
@project_settings.route('/Settings')
def show():
    try:
        return render_template('pages/settings.html')
    except TemplateNotFound:
        abort(404)
