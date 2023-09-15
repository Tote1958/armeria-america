from app.models import Supplier
from app.repositories import SupplierRepository

class SupplierService:
    def __init__(self):
        self.__repo = SupplierRepository()
    
    def fin(self, id) -> Supplier:
        return self.__repo.find_by_id(id)
    
    def create(self, entity: Supplier) -> Supplier:
        return self.__repo.create(entity)
    
    def update(self, entity: Supplier, id:int) -> Supplier:
        return self.__repo.update(entity, id)
    


    def find_all(self) -> []: #es un parametro de salida
        list_supplier = []
        supplier1 = Supplier()
        supplier1.code = '1321233215'
        supplier1.cuil = '203211526305'
        supplier1.email = 'dante07082001@gmail.com'
        list_supplier.append( supplier1 )
        return list_supplier