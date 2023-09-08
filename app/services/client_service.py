from app.models import Client
class ClientService:
    def __init__(self):
        pass
    def find_all(self) -> []:
        list_client =[]
        client1 = Client('Santino', '32123543', '1234', 'Sarmiento 321', 'santino@gmail.com')
        client1.name
        client1.code
        client1.dni
        client1.address
        client1.email
        list_client.append()
        return list_client