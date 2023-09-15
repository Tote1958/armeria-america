from app.models.supplier import Supplier
from marshmallow import validate, fields, Schema, post_load

class SupplierSchema(Schema):
    id = fields.Integer(dump_only=True) #dump_only es para que la info que envie al cliente se muestre 
    name = fields.String(required=True)
    cuil = fields.String(required=True)
    email = fields.String(required=True, validate=validate.Email())
    code = fields.String(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return Supplier(**data) # los asteriscos hacen que vincule los esquemas con los modelos 