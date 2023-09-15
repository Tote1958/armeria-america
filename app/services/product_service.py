from app.models import Product
from app.repositories import ProductRepository

class ProductService:

    def __init__(self):
        self.__repo = ProductRepository()

    def find_by_name(self, productname) -> Product:
        return self.__repo.find_by_productname(productname)
    
    def create(self, entity: Product) -> Product:
        return self.__repo.create(entity)

    def update(self, entity: Product, id: int) -> Product:
        return self.__repo.update(entity, id)

    def find_all(self) -> []:
        list_product = []
        product1 = Product()
        product1.name = 'Product Name'
        product1.caliber = '45'
        product1.brand = 'Cold'
        product1.description = 'Condición: Nuevo'
        product1.type = 'Munción'
        product1.serial_number = '122-AWE'
        list_product.append(product1)
        return list_product