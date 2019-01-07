__author__ = 'Muhammad Abdullah Mughal'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

from flask import Blueprint, request, jsonify
from core.processing.file.storage import Storage

ajax_sample_upload = Blueprint('upload_sample', __name__, template_folder='templates')


@ajax_sample_upload.route('/upload_sample', methods=['GET', 'POST'])
def upload_sample():
    if request.method == 'POST':
        file = request.files['file']
        storage_object = Storage(file)
        results = storage_object.process_file()
        return jsonify(results)
