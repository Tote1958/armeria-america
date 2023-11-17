from flask import Blueprint, jsonify, request
from app.services.supplier_service import SupplierService
from ..mapping.supplier_schema import SupplierSchema
from ..models.response_message import ResponseBuilder
from ..mapping.response_schema import ResponseSchema

service = SupplierService()
supplier_schema_many = SupplierSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
supplier_schema = SupplierSchema()
response_schema = ResponseSchema() 
supplier = Blueprint('supplier', __name__)


@supplier.route('/supplier/', methods=['GET'])
def index(): #anduvo
    list = service.find_all()
    result = supplier_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@supplier.route('/supplier/id/<int:id>', methods=['GET']) #en <int:id> pongo el id que quiero buscar
def find_by_id(id): #anduvo
    response_builder = ResponseBuilder("Usuario encontrado", 100, supplier_schema.dump(service.find_by_id(id)))
    return response_schema.dump((response_builder.build())), 200

@supplier.route('/supplier/create', methods=['POST'])
def create_supplier(): #anduvo
    supplier = supplier_schema.load(request.json)
    return {"supplier": supplier_schema.dump(service.create(supplier))}, 200

@supplier.route('/supplier/search/', methods=['GET'])
def find_by_name(): #anduvo
     name = request.args.get('name')
     response_builder = ResponseBuilder()
     response = supplier_schema_many.dump(service.find_by_name(name))
     if response:
         response_builder.add_message("Nombre encontrado").add_status_code(100).add_data({'supplier': response})
         return response_schema.dump((response_builder.build())), 200
     else:
         response_builder.add_message("No se encontro el nombre").add_status_code(400).add_data(response)
         return response_schema.dump((response_builder.build())), 400
    

@supplier.route('/supplier/email/<string:email>', methods=['GET'])
def find_by_email(email): #anduvo
    response = supplier_schema.dump(service.find_by_email(email))
    if response:
        response_builder = ResponseBuilder("Email encontrado",100, supplier_schema.dump(service.find_by_email(email)))
        return response_schema.dump((response_builder.build())), 200
    else:
        response_builder = ResponseBuilder("No se encontro el email", 400, supplier_schema.dump(service.find_by_email(email)))
        return response_schema.dump((response_builder.build())), 400

@supplier.route('/supplier/update/<int:id>', methods=['PUT'])
def update(id): #anduvo
    response_builder = ResponseBuilder()
    supplier = request.json
    return {"supplier":supplier_schema.dump(service.update(supplier, id))}, 200

@supplier.route('/supplier/delete/<int:id>', methods=['DELETE'])
def delete_supplier(id): #anduvo
    response_builder = ResponseBuilder()
    response_builder.add_message('Proveedor eliminado').add_status_code(200).add_data(supplier_schema.dump(service.delete(id)))
    return response_schema.dump(response_builder.build()), 200             