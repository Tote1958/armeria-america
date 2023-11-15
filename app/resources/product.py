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
    response_builder = ResponseBuilder("Producto", 100, product_schema.dump(service.find_by_id(id))) # porque 100 y no 200 el status_code??
    # response_builder.status_code = 200
    # return response_builder
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/name/<string:name>', methods=['GET'])
def find_by_name(name):
    service = ProductService()
    list = service.find_by_name(name)
    response_builder = ResponseBuilder("Producto", 100, product_schema_many.dump(list))
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/caliber/<string:caliber>', methods=['GET'])
def find_by_caliber(caliber):
    service = ProductService()
    list = service.find_by_caliber(caliber)
    response_builder = ResponseBuilder("Calibre", 100, product_schema_many.dump(list))
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/brand/<string:brand>', methods=['GET'])
def find_by_brand(brand):
    service = ProductService()
    list = service.find_by_brand(brand)
    response_builder = ResponseBuilder("Marca", 100, product_schema_many.dump(list))
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/type/<string:type>', methods=['GET'])
def find_by_type(type):
    service = ProductService()
    list = service.find_by_type(type)
    response_builder = ResponseBuilder("Tipo", 100, product_schema_many.dump(list))
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/serial_number/<string:serial_number>', methods=['GET'])
def find_by_serial_number(serial_numb):
    service = ProductService()
    list = service.find_by_serial_number(serial_numb)
    response_builder = ResponseBuilder("Numero de serie", 100, product_schema_many.dump(list))
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/add', methods=['POST'])
def create_product():
    service = ProductService()
    product = product_schema.load(request.json)
    # response_builder = ResponseBuilder()
    # response_builder.add_message('Producto creado!!').add_status_code(200).add_data(product_schema.dump(service.find(id)))
    # return response_schema.dump(response_builder.build()), 200
    status_code = 200
    return {'product': product_schema.dump(service.create(product))}, status_code

@product.route('/products/update/<int:id>', methods=['PUT'])
def update_product(id):
    service = ProductService()
    product = request.json # obtiene el objeto JSON de la solicitud. Serían los nuevos datos
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto actualizado!!').add_status_code(200).add_data(product_schema.dump(service.update(product, id))) # Preguntar la dif entre status 100 y 200
    return response_schema.dump(response_builder.build()), 200

@product.route('/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    service = ProductService()
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto eliminado.').add_status_code(200).add_data(product_schema.dump(service.delete(product, id)))
    return response_schema.dump(response_builder.build()), 200