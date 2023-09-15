from app.models import ProductType
from app.config.database import db 
from app.repositories.CRUD import Create, Read, Update, Delete

class ClientRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        pass

    def find_by_id(self, id: int) -> ProductType:
        pass

    def find_by_name(self, name: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.name == name).one()
    
    def find_by_id(self, name: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.id == name).one()