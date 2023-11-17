from app.models import Supplier 
from app.config.database import db
from .CRUD import Create, Read, Update, Delete


class SupplierRepository(Read, Update, Create, Delete):

    def __init__(self):
        self.__model = Supplier
    
    
    def find_all(self): 
        return db.session.query(self.__model).all()

    def find_by_id(self, id: int) -> Supplier: #Read
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def create(self, supplier: Supplier) -> db.Model: 
        db.session.add(supplier)
        db.session.commit()
        return supplier
    
    def find_by_name(self, name: str) -> list:
        list = db.session.query(self.__model).filter(self.__model.name.like(name)).all() 
        return list
    
    def delete(self, id: int):
        entity = self.find_by_id(id) 
        db.session.delete(entity)
        db.session.commit()
        return entity
    
    def find_by_email(self, email: str) -> Supplier:
        return db.session.query(self.__model).filter(self.__model.email == email).first() 
    
    def update(self,dto, id: int) -> Supplier: # data transfer object(dto)
        entity = self.find_by_id(id)
        try:
            entity.name = dto["name"]
        except:
            pass
        try:
            entity.email = dto["email"]
        except:
            pass
        try:
            entity.cuil = dto["cuil"]
        except:
            pass
        try:
            entity.code = dto["code"]
        except:
            pass
        db.session.commit()
        return entity
    