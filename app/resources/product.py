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

@product.route('/products/id/<int:id>', methods=['GET'])
def find_by_id(id):
    service = ProductService()
    object = service.find_by_id(id)
    product = product_schema.dump(object)
    resp = jsonify(product)
    resp.status_code = 200
    return resp

@product.route('/products/by_name', methods=['GET'])
def index():
    service = ProductService()
    list = service.find_all()                       # Preguntar al profe como filtrar por nombre
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp

'''
 faltaría:
  por calibre (caliber)
  por marca (brand)
  por tipo (type)
  por numero de serie (serial_number)
'''