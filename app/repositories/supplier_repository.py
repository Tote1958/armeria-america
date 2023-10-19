from functools import update_wrapper
from app.models import Supplier #En el repository va la comunicacion con la base de datos
from app import db
from .CRUD import Create, Read, Update, Delete

class SupplierRepository(Read, Update, Create, Delete):

    def __init__(self):
        self.__model = Supplier
    
    
    def find_all(self): #Read
        return db.session.query(self.__model).all()

    def find_by_id(self, id: int) -> Supplier: #Read
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def update(self, supplier: Supplier, id: int) -> Supplier: #Update
        entity = self.find_by_id(id)
        entity.name = supplier.name
        entity.email = supplier.email
        entity.code = supplier.code
        entity.cuil = supplier.cuil
        entity.id = supplier.id
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def create(sef, supplier: Supplier) -> db.Model: #Create
        db.session.add(supplier)
        db.session.commit()
        return supplier
    
    def find_by_name(self, name: str) -> Supplier:
        return db.session.query(self.__model).filter(self.__model.name == name)
    
    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity
    
    def find_by_email(self, email: str) -> Supplier:
        return db.session.query(self.__model).filter(self.__model.name == email).like() #like busca la concidencia