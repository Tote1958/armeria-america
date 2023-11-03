from app.models import ProductType
from app.config.database import db 
from .CRUD import Create, Read, Update, Delete

class ProductTypeRepository(Create, Read, Update, Delete):
    def __init__(self):
        self.__model = ProductType

    #Create
    def create(self, dto: ProductType) -> db.model:
        # entity = ProductType(name=dto['name'], code=dto['code'], description=dto['description'])
        db.session.add(dto)
        db.session.commit()
        return dto

    #Read
    def find_by_id(self, id: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.id == id).one()

    def find_by_name(self, name: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.name == name).one()
    
    def find_by_code(self, code: str) -> ProductType:
        return db.session.query(self.__model).filter(self.__model.code == code).one()
    
    def find_all(self):
        return db.session.query(self.__model).all()
    
    #Update
    def update(self, productType, id: int) -> ProductType:
        entity = self.find_by_id(id)
        if productType.name:
            entity.name = productType.name
        if productType.code:
            entity.code = productType.code
        if productType.description:
            entity.description = productType.description
        db.session.add(entity)
        db.session.commit()
        return entity
    
    #Delete
    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()