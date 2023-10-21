from app.services.command import TareaCommand

class ReserveService(TareaCommand):

    def __init__(self):
        pass

    def execute(self,user):
        return
    
    def reserve_product(self,product,user):
        print(f"{product.name} registrado a {user.name}")