from flask import Blueprint, jsonify
from app.services.supplier_service import SupplierService
from ..mapping.supplier_schema import SupplierSchema

ps = SupplierSchema(many=True) # es para varios parametros
supplier = Blueprint('supplier', __name__)

@supplier.route('/supplier/', methods=['GET'])
def index():
    service = SupplierService()
    lista = service.find_all()
    resp = jsonify('OK PROVEEDORES')
    resp.status_code = 200
    return resp