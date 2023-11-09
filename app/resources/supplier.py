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
def index(): #anduvo
    service = SupplierService()
    list = service.find_all()
    result = supplier_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@supplier.route('/supplier/id/<int:id>', methods=['GET']) #en <int:id> pongo el id que quiero buscar
def find_by_id(id): #anduvo
    service = SupplierService()
    response_builder = ResponseBuilder("Usuario encontrado", 100, supplier_schema.dump(service.find_by_id(id)))
    return response_schema.dump((response_builder.build())), 200

@supplier.route('/supplier/create', methods=['POST'])
def create_supplier(): #anduvo
    service = SupplierService()
    supplier = supplier_schema.load(request.json)
    return {"supplier": supplier_schema.dump(service.create(supplier))}, 200

@supplier.route('/supplier/name/<string:name>', methods=['GET'])
def find_by_name(name):
    service = SupplierService()
    object = service.find_by_name(name)
    result = supplier_schema.dump(object)
    return jsonify(result), 200

@supplier.route('/supplier/email/<string:email>', methods=['GET'])
def find_by_email(email):
    service = SupplierService()
    response = supplier_schema.dump(service.find_by_email(email))
    if response:
        response_builder = ResponseBuilder("Email encontrado",100, supplier_schema.dump(service.find_by_email(email)))
        return response_schema.dump((response_builder.build())), 200
    else:
        response_builder = ResponseBuilder("No se encontro el email", 400, supplier_schema.dump(service.find_by_email(email)))
        return response_schema.dump((response_builder.build())), 400

@supplier.route('/supplier/update/<int:id>', methods=['PUT'])
def update(id):
    service = SupplierService()
    supplier = request.json
    return {"supplier":supplier_schema.dump(service.update(supplier, id))}, 200

@supplier.route('/supplier/delete/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    service = SupplierService()
    return {"delete supplier": supplier_schema.dump(service.delete(id))}, 200                