from app.models import Supplier

class SupplierService:
    def __init__(self):
        pass

    def find_all(self) -> []: #es un parametro de salida
        list_supplier = []
        supplier1 = Supplier()
        supplier1.code = '1321233215'
        supplier1.cuil = '203211526305'
        supplier1.email = 'dante07082001@gmail.com'
        list_supplier.append( supplier1 )
        return list_supplier