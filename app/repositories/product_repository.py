from app.models import Product
from app.config.database import db
from .CRUD import Create, Read, Update, Delete

class ProductRepository(Create, Read, Update, Delete):
    def __init__(self):
        self.__model = Product
    
    def create():
        pass

    def find_by_id(self, id: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def find_by_name(self, name: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.name == name).one()