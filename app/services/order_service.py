from app.services.command import TareaCommand

class OrderService(TareaCommand):

    def __init__(self):
        #TODO: configuración de servidor de correo
        pass

    def execute(self, model):
        self.sending_order(model.email, 'Orden enviada')

    def sending_order(self, email, message):
        #TODO: Se envía un email e imprime un mensaje
        print(f'{message} and the mail {email}')