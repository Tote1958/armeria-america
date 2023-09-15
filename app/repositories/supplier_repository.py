from functools import update_wrapper
from app.models import Supplier
from app import db
from .CRUD import Create, Read, Update, Delete

class SupplierRepository(Read):

    def __init__(self):
        self.__model = Supplier
    
    def find_all(self):
        return db.session.query(self.__model).all()

    def find_by_id(self, id: int) -> Supplier:
        return db.session.query(self.__model).filter(self.__model.id == id).one()