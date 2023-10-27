from flask import Blueprint, jsonify, request
from app.services.productType_service import ProductTypeService
from app.mapping.productType_schema import ProductTypeSchema
from ..mapping.response_schema import ResponseSchema

productType_schema_many = ProductTypeSchema(many=True) # many=True significa que se espera una lista de objetos
productType_schema = ProductTypeSchema()
response_schema = ResponseSchema()
productType = Blueprint('productType', __name__)

@productType.route('/productType/', methods=['GET'])
def index():
    service = ProductTypeService()
    list = service.find_all()
    result = productType_schema_many.dump(list) # ps.dump(list) es para cuando se espera una lista de objetos y dump es para convertir el objeto en un diccionario
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@productType.route('/productType/id/<int:id>', methods=['GET'])
def find_by_id(id):
    service = ProductTypeService()
    object = service.find_by_id(id)
    productType = productType_schema.dump(object) # productType_schema.dump(object) es para cuando se espera un solo objeto y dump es para convertir el objeto en un diccionario
    resp = jsonify(productType)
    resp.status_code = 200
    return resp

@productType.route('/productType/name/<string:name>', methods=['GET'])
def find_by_name(name):
    service = ProductTypeService()
    object = service.find_by_name(name)
    productType = productType_schema.dump(object)
    resp = jsonify(productType)
    resp.status_code = 200
    return resp

@productType.route('/productType/code/<string:code>', methods=['GET'])
def find_by_code(code):
    service = ProductTypeService()
    object = service.find_by_code(code)
    productType = productType_schema.dump(object)
    resp = jsonify(productType)
    resp.status_code = 200
    return resp

@productType.route('/productType/create/', methods=['POST'])
def create_productType():
    service = ProductTypeService()
    product = ProductTypeSchema.load(request.json)
    # response_builder = ResponseBuilder()
    # response_builder.add_message('Producto creado!!').add_status_code(200).add_data(product_schema.dump(service.find(id)))
    # return response_schema.dump(response_builder.build()), 200
    status_code = 200
    return {'product': productType_schema.dump(service.create(product))}, status_code