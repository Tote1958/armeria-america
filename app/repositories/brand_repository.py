from app.models import Brand
from app.config.database import db 
from .CRUD import Create, Read, Update, Delete


class BrandRepository(Create, Read, Update, Delete):

    def __init__(self):
        self.__model = Brand

    # dto: data transfer object
    def create(self, dto: Brand) -> db.Model:
        # entity = Brand(name=dto['name'], origin=dto['origin'])
        db.session.add(dto)
        db.session.commit()
        return dto
    
    def update(self, dto, id: int) -> Brand:
        entity = self.find_by_id(id)
        for key, value in dto.items():
            setattr(entity, key, value)
        db.session.commit()
        return entity

    def find_by_name(self, name: str) -> list:
        brands = db.session.query(self.__model).filter(self.__model.name.like(name)).all()
        return brands

    
    def find_all(self):
        return db.session.query(self.__model).all()
    
    def find_by_id(self, id: int) -> Brand:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity
