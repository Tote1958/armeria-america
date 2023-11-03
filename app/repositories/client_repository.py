from app.models import Client
from app.config.database import db 
from .CRUD import Create, Read, Update, Delete


class ClientRepository(Create, Read, Update, Delete):
    
    def __init__(self):
        self.__model = Client

    # dto: data transfer object
    def create(self, dto: Client) -> db.Model:
        # entity = Client(name=dto['name'], dni=dto['dni'],
        # code=dto['code'], address=dto['address'], email=dto['email'])
        db.session.add(dto)
        db.session.commit()
        return dto
    
    def update(self, dto, id: int) -> Client:
        entity = self.find_by_id(id)
        try:
            entity.name = dto['name']
        except:
            pass
        try:
            entity.email = dto['email']
        except:
            pass
        try:
            entity.address = dto['address']
        except:
            pass
        try:
            entity.code = dto['code']
        except:
            pass
        db.session.commit()
        return entity

    def find_by_name(self, name: str) -> Client:
        list = db.session.query(self.__model).filter(self.__model.name == name).first() # Ver donde poner el like
        return list
    
    def find_by_email(self, email: str) -> Client:
        return db.session.query(self.__model).filter(self.__model.email == email).first() # Ver donde poner el like

    
    def find_all(self):
        return db.session.query(self.__model).all()
    
    def find_by_id(self, id: int) -> Client:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity