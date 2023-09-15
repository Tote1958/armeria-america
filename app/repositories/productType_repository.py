from app.models import ProductType
from app.config.database import db 
from .CRUD import Create, Read, Update, Delete

class ProductTypeRepository(Create, Read, Update, Delete):
    def __init__(self):
        self.__model = ProductType

    def find_by_name(self, name: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.name == name).one()
    
    def find_by_id(self, id: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.id == id).one()