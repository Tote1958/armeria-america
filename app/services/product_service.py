from app.models import Product

class ProductService:

    def __init__(self):
        pass

    def find_all(self) -> []:
        list_product = []
        product1 = Product()
        product1.name = 'Product Name'
        product1.caliber = '45'
        product1.brand = 'Cold'
        product1.description = 'Condición: Nuevo'
        product1.type = 'Muncion'
        product1.serial_number = '122-AWE'
        list_product.append(product1)
        return list_product
        #list = []
        #list.append(repositories.find.all())
        #product = Product.objects.all()
        # FALTA
    #def find_by_serial_number(self, serial_number):
        #print()