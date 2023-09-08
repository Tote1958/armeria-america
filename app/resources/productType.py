from flask import Blueprint, jsonify
from services.productType_service import ProductTypeService

productType = Blueprint('productType', __name__)

@productType.route('/productType/', methods=['GET'])
def index():
    service = ProductTypeService()
    lista = service.find_all()
    resp = jsonify('OK desde productType')
    resp.status_code = 200
    return resp