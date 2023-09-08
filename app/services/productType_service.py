from app.models import ProductType

class ProductTypeService:
    def __init__(self):
        pass
    '''
    return a list of all product types
    '''
    def get_all(self) -> []:
        list_product_type = []
        productType1 = ProductType('Silenciador', 'SR', 'Silenciador monolitico')
        productType2 = ProductType('Mira', 'MA', 'Mira termica')
        productType3 = ProductType('Fusil de Asalto', 'FA', 'Fusil de asalto de 5.56')
        return self.__repo.find_all()
