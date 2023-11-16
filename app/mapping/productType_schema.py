from app.models.product_type import ProductType
from marshmallow import validate, fields, Schema, post_load

#dump_only=True significa que no se puede escribir en el campo, solo leer
#required=True significa que el campo es obligatorio
#load_only=True significa que el campo solo se puede escribir, no leer
class ProductTypeSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=True, validate=validate.Length(min=1, max=256))
    code = fields.String(required=True, validate=validate.Length(min=1, max=8))

    @post_load
    def make_productType(self, data, **kwargs):
        return ProductType(**data)