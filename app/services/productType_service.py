from app.models import ProductType
from app.repositories import ProductTypeRepository

class ProductTypeService:
    def __init__(self):
        self.__repo = ProductTypeRepository()
    '''
    return a list of all product types
    '''

    #Create
    def create(self, entity: ProductType):
        return self.__repo.create(entity)
    
    #Read
    def find_all(self) -> []:
        # list_product_type = []
        # productType1 = ProductType('Silenciador', 'SR', 'Silenciador monolitico')
        # productType2 = ProductType('Mira', 'MA', 'Mira termica')
        # productType3 = ProductType('Fusil de Asalto', 'FA', 'Fusil de asalto de 5.56')
        return self.__repo.find_all()
    
    def find_by_id(self, id) -> ProductType:
        return self.__repo.find_by_id(id)
    
    def find_by_name(self, name):
        return self.__repo.find_by_name(name)
    
    def find_by_code(self, code):
        return self.__repo.find_by_code(code)

    #Update    
    def update(self, entity: ProductType, id: int) -> ProductType:
        return self.__repo.update(entity, id)
    
    #Delete
    def delete(self, id: int):
        return self.__repo.delete(id)
