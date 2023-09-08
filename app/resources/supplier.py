from flask import Blueprint, jsonify
from app.services.supplier_service import SupplierService

supplier = Blueprint('supplier', __name__)

@supplier.route('/supplier/', methods=['GET'])
def index():
    service = SupplierService()
    lista = SupplierService.find_all()
    resp = jsonify('OK PROVEEDORES')
    resp.status_code = 200
    return resp