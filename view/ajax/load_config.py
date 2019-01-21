__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from flask import Blueprint, request, jsonify
from core.processing.config_parsing.configuration import Configuration

ajax_load_config = Blueprint('load_config', __name__, template_folder='templates')


@ajax_load_config.route('/load_config', methods=['GET', 'POST'])
def load_config():
    obj = Configuration()
    apikey = obj.get_virustotal_apikey()
    return jsonify({'apikey': apikey})
