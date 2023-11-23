from app.models import ProductType
from app.config.database import db 
from .CRUD import Create, Read, Update, Delete

class ProductTypeRepository(Create, Read, Update, Delete):
    def __init__(self):
        self.__model = ProductType

    """Recibe un JSON con los datos del tipo de producto y lo guarda en la base de datos"""
    #Create
    def create(self, dto: ProductType) -> db.Model:
        # entity = ProductType(name=dto['name'], code=dto['code'], description=dto['description'])
        db.session.add(dto)
        db.session.commit()
        return dto

    """Hacemos una busqueda por id del tipo de producto"""
    #Read
    def find_by_id(self, id: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.id == id).one()

    """Hacemos una busqueda por nombre del tipo de producto"""
    def find_by_name(self, name: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.name == name).one()

    """Hacemos una busqueda por codigo del tipo de producto"""    
    def find_by_code(self, code: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.code == code).one()

    """Hacemos una busqueda y nos trae todos los tipos de productos"""    
    def find_all(self):
        return db.session.query(self.__model).all()

    """Recibe un JSON con los datos del tipo de producto y lo modifica en la base de datos""" 
    #Update
    def update(self, dto, id: int) -> ProductType:
        entity = self.find_by_id(id)
        for key, value in dto.items():
            setattr(entity, key, value)
        db.session.commit()
        return entity
    
    """Borramos el tipo de producto por su id"""
    #Delete
    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()