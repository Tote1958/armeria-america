from command import TareaCommand


class RegisterProduct(TareaCommand):
    def __init__(self):
        pass


    def execute(self, model):
        self.registering_product(model.name, "WELCOME TO THE JUNGLE")

    def registering_product(self, product):
        print(f'{product} registrado')