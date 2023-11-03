from flask import Blueprint, jsonify, request
from app.services.client_service import ClientService
from ..mapping.client_schema import ClientSchema
from ..models.response_message import ResponseBuilder
from app.mapping.response_schema import ResponseSchema

client_schema_many = ClientSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
client_schema = ClientSchema()
response_schema = ResponseSchema()
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
    response_builder = ResponseBuilder("Usuario encontrado", 100, client_schema.dump(service.find_by_id(id)))
    # Preguntar si esta bien esta forma, esta forma anda
    return response_schema.dump((response_builder.build())), 200


@client.route('/client/create/', methods=['POST'])
def create_client():
    service = ClientService()
    client = client_schema.load(request.json)
    return {"client": client_schema.dump(service.create(client))}, 200


@client.route('/client/name/<string:name>', methods=['GET'])
def find_by_name(name):
    service = ClientService()
    object = service.find_by_name(name)
    result = client_schema.dump(object)
    return jsonify(result), 200


@client.route('/client/email/<string:email>', methods=['GET'])
def find_by_email(email):
    service = ClientService()
    response = client_schema.dump(service.find_by_email(email))
    if response:
        response_builder = ResponseBuilder("Email encontrado", 100, client_schema.dump(service.find_by_email(email)))
        # Preguntar si esta bien esta forma, esta forma anda
        return response_schema.dump((response_builder.build())), 200
    else:
        response_builder = ResponseBuilder("No se encontro el email", 400, client_schema.dump(service.find_by_email(email)))
        return response_schema.dump((response_builder.build())), 400


@client.route('/client/update/<int:id>', methods=['PUT'])
def update_client(id):
    service = ClientService()
    client = request.json
    return {"client": client_schema.dump(service.update(client, id))}, 200

@client.route('/client/update/<int:id>', methods=['DELETE'])
def update_client(id):
    service = ClientService()
    return {"deleted client": client_schema.dump(service.delete(id))}, 200
@client.route('/search', methods=['GET'])
def search():
    try:
        name = request.args.get('name')
    except:
        print('error')
    