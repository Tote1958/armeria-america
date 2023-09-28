from app.models import Supplier
from app.config.database import db
from app.repositories import SupplierRepository

class SupplierService:
    def __init__(self):
        self.__repo = SupplierRepository()
    
    def find_by_id(self, id) -> Supplier:
        return self.__repo.find_by_id(id)


    def find_all(self) -> []: #es un parametro de salida
        list_supplier = []
        name = 'dante'
        code = '1321233215'
        cuil = '203211526305'
        email = 'dante07082001@gmail.com'
        supplier1 = Supplier(name, cuil, email, code)
        list_supplier.append( supplier1 )
        return list_supplier
    