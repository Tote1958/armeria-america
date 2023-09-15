from flask import Blueprint, jsonify
from app.services.client_service import ClientService
from ..mapping.client_schema import ClientSchema

client_schema_many = ClientSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
client_schema = ClientSchema()
client = Blueprint('client', __name__)

@client.route('/client/', methods=['GET'])
def index():
    service = ClientService()
    list = service.find_all()
    result = client_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

