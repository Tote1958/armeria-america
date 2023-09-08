from app.models.Client import Client
from marshmallow import validate, fields, Schema, post_load

class ClientSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(load_only=True) #Hace que lo cargue pero que no lo muestre (es un dato sensible)

    @post_load
    def make_user(self, data, **kwargs):
        return Client(**data)