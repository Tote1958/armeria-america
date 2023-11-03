from app.models import Supplier #En el repository va la comunicacion con la base de datos
from app.config.database import db
from .CRUD import Create, Read, Update, Delete
# es la ultima capa que esta al final con la base de datos, la que rosa con la base de datos

class SupplierRepository(Read, Update, Create, Delete):

    def __init__(self):
        self.__model = Supplier
    
    
    def find_all(self): #Read
        return db.session.query(self.__model).all()

    def find_by_id(self, id: int) -> Supplier: #Read
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def create(sef, supplier: Supplier) -> db.Model: #Create
        db.session.add(supplier)
        db.session.commit()
        return supplier
    
    def find_by_name(self, name: str) -> Supplier:
        list = db.session.query(self.__model).filter(self.__model.name == name).first()
        return list
    
    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity
    
    def find_by_email(self, email: str) -> Supplier:
        return db.session.query(self.__model).filter(self.__model.name == email).like() #like busca la concidencia
    
    def update(self,dto, id: int) -> Supplier: # data transfer object(dto) = es para pasar objectos
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
            entity.cuil = dto['cuil']
        except:
            pass
        try:
            entity.code = dto['code']
        except:
            pass
        db.session.commit()
        return entity
    
    def delete(self, id:int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity