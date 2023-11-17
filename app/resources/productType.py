from flask import Blueprint, jsonify, request
from app.services.productType_service import ProductTypeService
from app.mapping.productType_schema import ProductTypeSchema
from ..mapping.response_schema import ResponseSchema
from ..models.response_message import ResponseBuilder

productType_schema_many = ProductTypeSchema(many=True) # many=True significa que se espera una lista de objetos
productType_schema = ProductTypeSchema()
response_schema = ResponseSchema()
productType = Blueprint('productType', __name__)
service = ProductTypeService()


#Create
@productType.route('/productType/create/', methods=['POST'])
def create_productType():
    response_builder = ResponseBuilder()
    product = productType_schema.load(request.json)
    response_builder.add_message('Producto creado!.').add_status_code(200).add_data(productType_schema.dump(service.create(product)))
    return response_schema.dump(response_builder.build()), 200
    # status_code = 200
    # return {'product': productType_schema.dump(service.create(product))}, status_code

#Read
@productType.route('/productType/', methods=['GET'])
def index():
    list = service.find_all()
    result = productType_schema_many.dump(list) # ps.dump(list) es para cuando se espera una lista de objetos y dump es para convertir el objeto en un diccionario
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@productType.route('/productType/id/<int:id>', methods=['GET'])
def find_by_id(id):
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto encontrado por id.').add_status_code(200).add_data(productType_schema.dump(service.find_by_id(id)))
    return response_schema.dump(response_builder.build()), 200
    # object = service.find_by_id(id)
    # productType = productType_schema.dump(object) # productType_schema.dump(object) es para cuando se espera un solo objeto y dump es para convertir el objeto en un diccionario
    # resp = jsonify(productType)
    # resp.status_code = 200
    # return resp

@productType.route('/productType/name/<string:name>', methods=['GET'])
def find_by_name(name):
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto encontrado por nombre.').add_status_code(200).add_data(productType_schema.dump(service.find_by_id(name)))
    return response_schema.dump(response_builder.build()), 200

@productType.route('/productType/code/<string:code>', methods=['GET'])
def find_by_code(code):
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto encontrado por codigo.').add_status_code(200).add_data(productType_schema.dump(service.find_by_id(code)))
    return response_schema.dump(response_builder.build()), 200
 
#Update
@productType.route('/productType/update/<int:id>', methods=['PUT'])
def update(id):
    productType = request.json
    return {"productType": productType_schema.dump(service.update(productType, id))}, 200

#Delete
@productType.route('/productType/delete/id/<int:id>', methods=['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    response_builder.add_message('Producto eliminado.').add_status_code(200).add_data(productType_schema.dump(service.delete(id)))
    return response_schema.dump(response_builder.build()), 200