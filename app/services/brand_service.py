from app.models import Brand
from app.repositories.brand_repository import BrandRepository


class BrandService:
    def __init__(self):
        self.__repo = BrandRepository()
        
    def find_all(self) -> Brand:
        return self.__repo.find_all()
    
    def find_by_id(self, id) -> Brand:
        return self.__repo.find_by_id(id)

    def find_by_name(self, name) -> Brand:
        return self.__repo.find_by_name(name)
    
    def find_by_origin(self, origin) -> Brand:
        return self.__repo.find_by_origin(origin)

    def create(self, entity: Brand) -> Brand:
        return self.__repo.create(entity)
    
    def update(self, dto, id: int) -> Brand:
        return self.__repo.update(dto, id)
    
    def delete(self, id: int) -> Brand:
        return self.__repo.delete(id)
    