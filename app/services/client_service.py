from app.models import Client
from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
class ClientService:
    def __init__(self):
        self.__repo = UserRepository()

    def find(self, id) -> Client:
        return self.__repo.find_by_id(id)
    
    def create(self, entity: Client) -> Client:
        entity.password = generate_password_hash( entity.password)
        return self.__repo.create(entity)
    
    def update(self, entity:Client, id:int) -> Client:
        return self.__repo.update(entity, id)
    

    
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
        