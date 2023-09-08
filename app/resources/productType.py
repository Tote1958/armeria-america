from flask import Blueprint, jsonify

productType = Blueprint('productType', __name__)

@productType.route('/productType/', methods=['GET'])
def index():
    resp = jsonify('OK desde productType')
    resp.status_code = 200
    return resp