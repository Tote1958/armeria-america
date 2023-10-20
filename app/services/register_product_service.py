from command import TareaCommand

class RegisterProduct(TareaCommand):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass