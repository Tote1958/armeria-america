from app.models.product import Product
from marshmallow import validate, fields, Schema, post_load

class ProductSchema(Schema):
    id = fields.Int(dump_only=True) #dump_only es para que la info que envío al cliente se muestre
    name = fields.String(required=True)
    caliber = fields.String(required=True) #required=True es porque se requiere que el cliente complete ese campo si o si
    brand = fields.String(required=True)
    description = fields.String(required=True)
    type = fields.String(required=True)
    serial_number = fields.String(required=True)
    
    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)