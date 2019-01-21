__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from flask import Blueprint, request, jsonify
from core.processing.config_parsing.configuration import Configuration

ajax_update_config = Blueprint('update_config', __name__, template_folder='templates')


@ajax_update_config.route('/update_config', methods=['GET', 'POST'])
def update_config():
    if request.method == 'POST':
        apikey = request.form['apikey']
        obj = Configuration()
        print(obj.update_virustotal_apikey(apikey))
        print(apikey)
    return jsonify({})
