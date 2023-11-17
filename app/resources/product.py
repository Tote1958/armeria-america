from flask import Blueprint, jsonify, request
from app.services.product_service import ProductService
from ..mapping.product_schema import ProductSchema
from ..models.response_message import ResponseBuilder
from ..mapping.response_schema import ResponseSchema

product_schema_many = ProductSchema(many=True) # many=True es para cuando tienen que recibir varios parametros
product_schema = ProductSchema()
response_schema = ResponseSchema()
product = Blueprint('product', __name__)
service = ProductService()

@product.route('/products/', methods=['GET'])
def index():
    list = service.find_all()
    products = product_schema_many.dump(list)
    resp = jsonify(products)
    resp.status_code = 200
    return resp

@product.route('/products/id/<int:id>', methods=['GET'])
def find_by_id(id):
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto encontrado por id.').add_status_code(200).add_data(product_schema.dump(service.find_by_id(id)))
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/search/', methods=['GET'])
def find_by_name():
    name = request.args.get('name')
    list = service.find_by_name(name)
    response = product_schema_many.dump(list)
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto').add_status_code(200).add_data({'products': response})
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/caliber/', methods=['GET'])
def find_by_caliber():
    caliber = request.args.get('caliber')
    list = service.find_by_caliber(caliber)
    response = product_schema_many.dump(list)
    response_builder = ResponseBuilder()
    response_builder.add_message("Calibre").add_status_code(100).add_data({'products': response})
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/brand/', methods=['GET'])
def find_by_brand():
    brand = request.args.get('brand')
    list = service.find_by_brand(brand)
    response = product_schema_many.dump(list)
    response_builder = ResponseBuilder()
    response_builder.add_message("Marca").add_status_code(100).add_data({'products': response})
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/type/', methods=['GET'])
def find_by_type():
    type = request.args.get('type')
    list = service.find_by_type(type)
    response = product_schema_many.dump(list)
    response_builder = ResponseBuilder()
    response_builder.add_message("Tipo").add_status_code(100).add_data({'products': response})
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/serial_number/<string:serial_number>', methods=['GET'])
def find_by_serial_number(serial_number):
    response_builder = ResponseBuilder()
    response = product_schema.dump(service.find_by_serial_number(serial_number))
    response_builder.add_message('Producto encontrado por id.').add_status_code(200).add_data(response)
    return response_schema.dump((response_builder.build())), 200

@product.route('/products/create', methods=['POST'])
def create_product():
    product = product_schema.load(request.json)
    # response_builder = ResponseBuilder()
    # response_builder.add_message('Producto creado!!').add_status_code(200).add_data(product_schema.dump(service.create(id)))
    # return response_schema.dump(response_builder.build()), 200
    status_code = 200
    return {'product': product_schema.dump(service.create(product))}, status_code

@product.route('/products/update/<int:id>', methods=['PUT'])
def update_product(id):
    product = request.json # obtiene el objeto JSON de la solicitud. Serían los nuevos datos
    return {"product_updated":product_schema.dump(service.update(product, id))}, 200

@product.route('/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto eliminado.').add_status_code(200).add_data(product_schema.dump(service.delete(id)))
    return response_schema.dump(response_builder.build()), 200