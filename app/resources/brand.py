from flask import Blueprint, jsonify, request
from app.services.brand_service import BrandService
from app.mapping.brand_schema import BrandSchema

brand_schema_many = BrandSchema(many=True)  # es para que devuelva varios objetos, este se usa para find_all
brand_schema = BrandSchema()
brand = Blueprint('brand', __name__)


@brand.route('/brand/', methods=['GET'])
def index():
    service = BrandService()
    list = service.find_all()
    result = brand_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@brand.route('/brand/id/<int:id>', methods=['GET'])
def find_by_id(id):
    service = BrandService()
    object = service.find_by_id(id)
    result = brand_schema.dump(object)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@brand.route('/brand/create/', methods=['POST'])
def create_brand():
    service = BrandService()
    brand = brand_schema.load(request.json)
    return {"brand": brand_schema.dump(service.create(brand))}, 200


@brand.route('/brand/name/<string:name>', methods=['POST'])
def find_by_name(name):
    service = BrandService()
    object = service.find_by_name(name)
    result = brand_schema.dump(object)
    return jsonify(result), 200


@brand.route('/brand/origin/<string:name>', methods=['POST'])
def find_by_origin(origin):
    service = BrandService()
    object = service.find_by_origin(origin)
    result = brand_schema.dump(object)
    return jsonify(result), 200
