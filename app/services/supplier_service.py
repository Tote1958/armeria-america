from app.models import Supplier #service va al repository
from app.repositories.supplier_repository import SupplierRepository

class SupplierService:
    def __init__(self):
        self.__repo = SupplierRepository()
    
    def find_by_id(self, id) -> Supplier:
        return self.__repo.find_by_id(id)
    
    def find_by_name(self, name) -> Supplier:
        return self.__repo.find_by_name(name)
    
    def find_by_email(self, email) -> Supplier:
        return self.__repo.find_by_email(email)
    
    def find_all(self) -> Supplier:
        return self.__repo.find_all()
    
    def create(self, entity: Supplier) -> Supplier:
        return self.__repo.create(entity)
    
    def update(self, entity: Supplier, id:int) -> Supplier:
        return self.__repo.update(entity, id)
    
    def delete(self, id:int) -> Supplier:
        return self.__repo.delete(id)

    # def find_all(self) -> []: #es un parametro de salida
    #     list_supplier = []
    #     name = 'dante'
    #     code = '1321233215'
    #     cuil = '203211526305'
    #     email = 'dante07082001@gmail.com'
    #     supplier1 = Supplier(name, cuil, email, code)
    #     list_supplier.append( supplier1 )
    #     return list_supplier
    