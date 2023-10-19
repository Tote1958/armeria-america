from flask import Blueprint, jsonify, request
from app.services.supplier_service import SupplierService
from ..mapping.supplier_schema import SupplierSchema
from ..models.response_message import ResponseBuilder
from ..mapping.response_schema import ResponseSchema

supplier_schema_many = SupplierSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
supplier_schema = SupplierSchema()
response_schema = ResponseSchema()
supplier = Blueprint('supplier', __name__)


@supplier.route('/supplier/', methods=['GET'])
def index():
    service = SupplierService()
    list = service.find_all()
    result = supplier_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@supplier.route('/supplier/id/<int:id>', methods=['GET'])
def find_by_id(id):
    service = SupplierService()
    object = service.find_by_id(id)
    result = supplier_schema.dump(object)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@supplier.route('/supplier/create', methods=['POST'])
def create_supplier():
    service = SupplierService()
    supplier = supplier_schema.load(request.json)
    response_builder = ResponseBuilder() #Checkear esto, transformar el mensaje con marshmallow, crea un objeto()
    response_builder.add_message('Usuario creado exitosamente').add_status_code(200).add_data(supplier_schema.dump(service.find(id)))
    return response_schema.dump(response_builder.build()), 200

@supplier.route('/suppler/name/<string:name>', methods=['POST'])
def find_by_name(name):
    service = SupplierService()
    object = service.find_by_name(name)
    result = supplier_schema.dump(object)
    return jsonify(result), 200

@supplier.route('/supplier/email/<string:email>', methods=['POST'])
def find_by_email(email):
    service = SupplierService()
    object = service.find_by_email(email)
    result = supplier_schema.dump(object)
    return jsonify(result), 200