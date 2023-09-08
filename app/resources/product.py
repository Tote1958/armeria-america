from flask import Blueprint, jsonify
from app.services.product_service import ProductService

product = Blueprint('product', __name__)

@product.route('/products/', methods=['GET'])
def index():
    service = ProductService()
    list = ProductService.find_all()
    resp = jsonify('OK PRODUCTOS')
    resp.status_code = 200
    return resp