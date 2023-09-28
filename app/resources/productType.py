from flask import Blueprint, jsonify
from app.services.productType_service import ProductTypeService
from app.mapping.productType_schema import ProductTypeSchema

productType_schema_many = ProductTypeSchema(many=True) # many=True significa que se espera una lista de objetos
productType_schema = ProductTypeSchema()
productType = Blueprint('productType', __name__)

@productType.route('/productType/', methods=['GET'])
def index():
    service = ProductTypeService()
    list = service.find_all()
    result = productType_schema_many.dump(list) # ps.dump(list) es para cuando se espera una lista de objetos y dump es para convertir el objeto en un diccionario
    resp = jsonify(result)

@productType.route('/productType/id/<int:id>', methods=['GET'])
def find_by_id(id):
    service = ProductTypeService()
    object = service.find_by_id(id)
    productType = productType_schema_many.dump(object) # ps.dump(object) es para cuando se espera un solo objeto y dump es para convertir el objeto en un diccionario
    resp = jsonify(productType)
    resp.status_code = 200
    return resp