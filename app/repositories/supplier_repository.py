from functools import update_wrapper
from app.models import Supplier
from app import db
from app.repositories import Read

class SupplierRepository(Read):

    def __init__(self):
        self.__model = Supplier

    def find_by_id(self, id: int) -> Supplier:
        return db.session.query(self.__model).filter(self.__model.id == id).one()