from app.models import Client
from app.config.database import db 
from .CRUD import Create, Read, Update, Delete

class ClientRepository(Read):
    
    def __init__(self):
        self.__model = Client

    def find_by_name(self, name: str) -> Client:
        return db.session.query(self.__model).filter(self.__model.name == name).one()
    
    def find_all(self):
        return db.session.query(self.__model).all()
    def find_by_id(self, id: str) -> Client:
        return db.session.query(self.__model).filter(self.__model.id == id).one()