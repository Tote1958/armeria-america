from app.models import Product
from app.config.database import db
from .CRUD import Create, Read, Update, Delete

class ProductRepository(Create, Read, Update, Delete):
    def __init__(self):
        self.__model = Product
    
    def create(self, dto: Product) -> db.Model:
        #entity = Product(name = product['name'], caliber = product['caliber'], brand = product['brand'], description = ['description'], type = ['type'], serial_number = ['serial_number'])
        db.session.add(dto)
        db.session.commit()
        return dto

    def update(self, dto, id: int) -> Product:
        entity = self.find_by_id(id)
        try:
            entity.name = dto['name']
        except:
            pass
        try:
            entity.caliber = dto['caliber']
        except:
            pass
        try:
            entity.brand = dto['brand']
        except:
            pass
        try:
            entity.description = dto['description']
        except:
            pass
        try:
            entity.type = dto ['type']
        except:
            pass
        try:
            entity.serial_number = dto ['serial_number']
        except:
            pass
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
        return db.session.query(self.__model).filter(self.__model.name == name).all()
    
    def find_by_caliber(self, caliber: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.caliber == caliber).all()
    
    def find_by_brand(self, brand: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.brand == brand).all()
    
    def find_by_type(self, type: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.type == type).all()
    
    def find_by_serial_number(self, serial_numb: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.serial_number == serial_numb).one()
  