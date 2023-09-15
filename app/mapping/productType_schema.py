from app.models.product_type import ProductType
from marshmallow import validate, fields, Schema, post_load

#dump_only=True significa que no se puede escribir en el campo, solo leer
#required=True significa que el campo es obligatorio
#load_only=True significa que el campo solo se puede escribir, no leer
class ProductTypeSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    code = fields.String(required=True)

    @post_load
    def make_productType(self, data, **kwargs):
        return ProductType(**data)