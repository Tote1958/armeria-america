from app.models import Client
from app.config.database import db 
from .CRUD import Create, Read, Update, Delete

class ClientRepository(Create, Read, Update, Delete):
    
    def __init__(self):
        self.__model = Client

    #dto: data transfer object
    def create(self, dto:Client) -> db.Model:
        #entity = Client(name=dto['name'], dni=dto['dni'], code=dto['code'], address=dto['address'], email=dto['email'])
        db.session.add(dto)
        db.session.commit()
        return dto
    
    def update(self, client: Client, id: int ) -> Client: 
        entity = self.find_by_id(id)
        entity.name = client.name
        entity.email = client.email
        entity.address = client.address
        entity.code = client.code
        db.session.add(entity)
        db.session.commit()
        return entity


    def find_by_name(self, name: str) -> Client:
        list = db.session.query(self.__model).filter(self.__model.name == name) # Ver donde poner el like
        return list
    
    def find_by_email(self, email: str) -> Client:
        list = db.session.query(self.__model).filter(self.__model.name == email).like() # Ver donde poner el like
        return list
    
    def find_all(self):
        return db.session.query(self.__model).all()
    
    def find_by_id(self, id: str) -> Client:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity