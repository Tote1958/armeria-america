from flask import Blueprint, jsonify
from app.services.brand_service import BrandService
from app.mapping.brand_schema import BrandSchema

ps = BrandSchema(many=True)
brand = Blueprint('brand',__name__)

@brand.route('/brand/', methods=['GET'])
def index():
    service = BrandService()
    lista = service.find_all()
    resp = jsonify('OK MARCA')
    resp.status_code = 200
    return resp