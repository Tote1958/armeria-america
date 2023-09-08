from flask import Blueprint, jsonify
from app.services.client_service import ClientService

client = Blueprint('client',__name__)

@client.route('/client/', methods=['GET'])
def index():
    service = ClientService()
    lista = ClientService.find_all()
    resp = jsonify('OK CLIENTE')
    resp.status_code = 200
    return resp