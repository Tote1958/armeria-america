from flask import Blueprint, jsonify, request
from app.services.brand_service import BrandService
from app.mapping.brand_schema import BrandSchema
from ..models.response_message import ResponseBuilder
from app.mapping.response_schema import ResponseSchema

brand_schema_many = BrandSchema(many=True)  # es para que devuelva varios objetos, este se usa para find_all
brand_schema = BrandSchema()
response_schema = ResponseSchema()
service = BrandService()
brand = Blueprint('brand', __name__)


@brand.route('/brand/', methods=['GET'])
def index():
    list = service.find_all()
    result = brand_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@brand.route('/brand/id/<int:id>', methods=['GET'])
def find_by_id(id):
    response_builder = ResponseBuilder()
    response = brand_schema.dump(service.find_by_id(id))
    if response:
        response_builder.add_message("Marca encontrado").add_status_code(100).add_data(response)
        return response_schema.dump((response_builder.build())), 200
    else:
        response_builder.add_message("No se encontro la marca").add_status_code(400).add_data(
            response)
        return response_schema.dump((response_builder.build())), 400

@brand.route('/brand/search/', methods=['GET'])
def find_by_name():
    name = request.args.get('name')
    response_builder = ResponseBuilder()
    response = brand_schema_many.dump(service.find_by_name(name))
    if response:
        response_builder.add_message("Nombre de la marca encontrado").add_status_code(100).add_data({'brands': response})
        return response_schema.dump((response_builder.build())), 200
    else:
        response_builder.add_message("No se encontro el nombre de la marca").add_status_code(400).add_data(
            response)
        return response_schema.dump((response_builder.build())), 400


@brand.route('/brand/create/', methods=['POST'])
def create_brand():
    response_builder = ResponseBuilder()
    brand = brand_schema.load(request.json)
    response_builder.add_message("Marca creada").add_status_code(100).add_data(brand_schema.dump(service.create(brand)))
    return response_schema.dump((response_builder.build())), 200

@brand.route('/brand/update/<int:id>', methods=['PUT'])
def update_brand(id):
    response_builder = ResponseBuilder()
    brand = request.json
    response_builder.add_message("Marca creada").add_status_code(100).add_data(brand_schema.dump(service.update(brand, id)))
    return response_schema.dump((response_builder.build())), 200

@brand.route('/brand/delete/<int:id>', methods=['DELETE'])
def delete_brand(id):
    response_builder = ResponseBuilder()
    response_builder.add_message('Marca eliminada.').add_status_code(200).add_data(brand_schema.dump(service.delete(id)))
    return response_schema.dump(response_builder.build()), 200