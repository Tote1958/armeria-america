from flask import Blueprint, jsonify

brand = Blueprint('brand',__name__)

@brand.route('/brand/', methods=['GET'])
def index():
    resp = jsonify('OK MARCA')
    resp.status_code = 200
    return resp