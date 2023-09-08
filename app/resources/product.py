from flask import Blueprint, jsonify
from app.services.product_service import ProductService
from ..mapping.product_schema import ProductSchema

ps = ProductSchema(many=True) # many=True es para cuando tienen que recibir varios parametros
product = Blueprint('product', __name__)

@product.route('/products/', methods=['GET'])
def index():
    service = ProductService()
    list = ProductService.find_all()
    resp = jsonify('OK PRODUCTOS')
    resp.status_code = 200
    return resp