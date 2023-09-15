from flask import Blueprint, jsonify
from app.services.client_service import ClientService
from ..mapping.client_schema import ClientSchema

ps = ClientSchema(many=True)

client = Blueprint('client',__name__)

@client.route('/client/', methods=['GET'])
def index():
    service = ClientService()
    lista = ClientService.find_all()
    resp = jsonify('OK CLIENTE')
    resp.status_code = 200
    return resp