from flask import Blueprint, jsonify

product = Blueprint('product', __name__)

@product.route('/products/', methods=('GET'))
def index():
    resp = jsonify('OK PRODUCTOS')
    resp.status_code = 200
    return resp