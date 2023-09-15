from flask import Blueprint, jsonify
from app.services.supplier_service import SupplierService
from ..mapping.supplier_schema import SupplierSchema

ps = SupplierSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
supplier = Blueprint('supplier', __name__)

@supplier.route('/supplier/', methods=['GET'])
def index():
    service = SupplierService()
    list = service.find_all()
    result = ps.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp