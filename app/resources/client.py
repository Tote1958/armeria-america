from flask import Blueprint, jsonify

client = Blueprint('client',__name__)

@client.route('/client/', methods=['GET'])
def index():
    resp = jsonify('OK CLIENTE')
    resp.status_code = 200
    return resp