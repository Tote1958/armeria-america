from flask import Blueprint, jsonify
from app.services.product_service import ProductService
from ..mapping.product_schema import ProductSchema

product_schema_many = ProductSchema(many=True) # many=True es para cuando tienen que recibir varios parametros
product_schema = ProductSchema()
product = Blueprint('product', __name__)

@product.route('/products/', methods=['GET'])
def index():
    service = ProductService()
    list = service.find_all()
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp