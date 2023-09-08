from app.models import ProductType

class ProductType_service:
    def __init__(self):
        pass
    def get_all(self) -> []:
        return self.__repo.find_all()
