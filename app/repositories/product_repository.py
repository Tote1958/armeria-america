from app.models import Product
from app.config.database import db
from .CRUD import Create, Read, Update, Delete

class ProductRepository(Create, Read, Update, Delete):
    def __init__(self):
        self.__model = Product
    
    def create(self, product: Product) -> Product:
        #entity = Product(name = product['name'], caliber = product['caliber'], brand = product['brand'], description = ['description'], type = ['type'], serial_number = ['serial_number'])
        db.session.add(product)
        db.session.commit()
        return product

    def update(self, product: Product, id: int) -> Product:
        entity = self.find_by_id(id)
        entity.name = product.name
        entity.caliber = product.caliber
        entity.brand = product.brand
        entity.description = product.description
        entity.type = product.type
        entity.serial_number = product.serial_number
        db.session.add(entity)
        db.session.commit()
        return entity 
    
    def delete(self, id: int) -> Product:
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity
    
    def find_all(self) -> Product:
        # return super().find_all()
        return db.session.query(self.__model).all()

    def find_by_id(self, id: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def find_by_name(self, name: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.name == name)