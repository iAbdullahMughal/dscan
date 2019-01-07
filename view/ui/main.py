__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/', defaults={'page': 'index'})
@index_page.route('/')
def show():
    try:
        return render_template('pages/home.html')
    except TemplateNotFound:
        abort(404)
