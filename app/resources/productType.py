from flask import Blueprint, jsonify
from app.services.productType_service import ProductTypeService
from app.mapping.productType_schema import ProductTypeSchema

ps = ProductTypeSchema(many=True) # many=True significa que se espera una lista de objetos
productType = Blueprint('productType', __name__)

@productType.route('/productType/', methods=['GET'])
def index():
    service = ProductTypeService()
    lista = service.find_all()
    resp = jsonify('OK desde productType')
    resp.status_code = 200
    return resp

@productType.route('/productType/id/<int:id>', methods=['GET'])
def find_by_id(id):
    service = ProductTypeService()
    object = service.find_by_id(id)
    productType = ps.dump(object) # ps.dump(object) es para cuando se espera un solo objeto y dump es para convertir el objeto en un diccionario
    resp = jsonify(productType)
    resp.status_code = 200
    return resp