from flask import Blueprint, jsonify, request
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


@client.route('/client/id/<int:id>', methods=['GET'])
def find_by_id(id):
    service = ClientService()
    object = service.find_by_id(id)
    result = client_schema.dump(object)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@client.route('/client/create/', methods=['POST'])
def create_client():
    service = ClientService()
    client = client_schema.load(request.json)
    return {"client": client_schema.dump(service.create(client))}, 200


@client.route('/client/name/<string:name>', methods=['POST'])
def find_by_name(name):
    service = ClientService()
    object = service.find_by_name(name)
    result = client_schema.dump(object)
    return jsonify(result), 200


@client.route('/client/email/<string:email>', methods=['POST'])
def find_by_email(email):
    service = ClientService()
    object = service.find_by_email(email)
    result = client_schema.dump(object)
    return jsonify(result), 200
