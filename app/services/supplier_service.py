from app.models import Supplier
from app.config.database import db

class SupplierService:
    def __init__(self):
        pass

    def find_all(self) -> []: #es un parametro de salida
        list_supplier = []
        
        name = 'dante'
        code = '1321233215'
        cuil = '203211526305'
        email = 'dante07082001@gmail.com'
        supplier1 = Supplier(name, cuil, email, code)
        list_supplier.append( supplier1 )
        """db.session.add_all(list_supplier) 
        db.session.commit()""" #Esto guarda ese usuario en la
        return list_supplier