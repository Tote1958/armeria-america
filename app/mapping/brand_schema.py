from app.models.brand import Brand
from marshmallow import validate, fields, Schema, post_load

class BrandSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    origin = fields.String(required=True)

    @post_load # decorador que convierte los json en objetos
    def make_brand(self, data, **kwargs):
        return Brand(**data)