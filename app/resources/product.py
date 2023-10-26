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
    list = service.find_by_name()
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp

@product.route('/products/caliber/<int:caliber>', methods=['GET'])
def find_by_caliber():
    service = ProductService()
    list = service.find_by_caliber()
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp

@product.route('/products/brand/<string:brand>', methods=['GET'])
def find_by_brand():
    service = ProductService()
    list = service.find_by_brand()
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp

@product.route('/products/type/<string:type>', methods=['GET'])
def find_by_type():
    service = ProductService()
    list = service.find_by_type()
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp

@product.route('/products/serial_number/<string:serial_number>', methods=['GET'])
def find_by_serial_number():
    service = ProductService()
    list = service.find_by_serial_number()
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp

@product.route('/products/add', methods=['POST'])
def create_product():
    service = ProductService()
    product = product_schema.load(request.json)
    # response_builder = ResponseBuilder()
    # response_builder.add_message('Producto creado!!').add_status_code(200).add_data(product_schema.dump(service.find(id)))
    # return response_schema.dump(response_builder.build()), 200
    status_code = 200
    return {'product': product_schema.dump(service.create(product))}, status_code
