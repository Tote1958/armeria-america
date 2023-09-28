from functools import update_wrapper
from app.models import Supplier
from app import db
from .CRUD import Create, Read, Update, Delete

class SupplierRepository(Read, Update, Create):

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
    
