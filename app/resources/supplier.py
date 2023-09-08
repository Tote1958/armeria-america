from flask import Blueprint, jsonify

supplier = Blueprint('supplier', __name__)

@supplier.route('/supplier/', methods=['GET'])
def index():
    resp = jsonify('OK PROVEEDORES')
    resp.status_code = 200
    return resp