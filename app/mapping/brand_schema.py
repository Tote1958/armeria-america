from app.models.brand import Brand
from marshmallow import validate, fields, Schema, post_load


class BrandSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=105))
    origin = fields.String(required=True, validate=validate.Length(min=1, max=105))

    @post_load # decorador que convierte los json en objetos
    def make_brand(self, data, **kwargs):
        return Brand(**data)