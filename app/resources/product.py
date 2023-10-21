from flask import Blueprint, jsonify, request
from app.services.product_service import ProductService
from ..mapping.product_schema import ProductSchema
from ..models.response_message import ResponseBuilder
from ..mapping.response_schema import ResponseSchema

product_schema_many = ProductSchema(many=True) # many=True es para cuando tienen que recibir varios parametros
product_schema = ProductSchema()
response_schema = ResponseSchema()
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

@product.route('/products/name/<string:name>', methods=['GET'])
def find_by_name():
    service = ProductService()
    list = service.find_by_name()                       # Preguntar al profe como filtrar por nombre
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp

@product.route('/products/add', methods=['POST'])
def post_product():
    service = ProductService()
    product = product_schema.load(request.json)
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto creado!!').add_status_code(200).add_data(product_schema.dump(service.find(id)))
    return response_schema.dump(response_builder.build()), 200

'''
 faltaría:
  por calibre (caliber)
  por marca (brand)
  por tipo (type)
  por numero de serie (serial_number)
'''