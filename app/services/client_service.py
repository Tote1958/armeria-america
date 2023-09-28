from app.models import Client
from app.repositories.client_repository import ClientRepository
class ClientService:
    def __init__(self):
        self.__repo = ClientRepository()
        
    def find_all(self) -> Client:
        return self.__repo.find_all()
    
    def find_by_id(self, id) -> Client:
        return self.__repo.find_by_id(id)
    

    def find_by_name(self, name) -> Client:
        return self.__repo.find_by_name(name)
    
    
    def create(self, entity: Client) -> Client:
        return self.__repo.create(entity)
    
    def update(self, entity:Client, id:int) -> Client:
        return self.__repo.update(entity, id)
    
    def delete(self, id:int) -> Client:
        return self.__repo.delete(entity, id)
    

    
"""    def test_create(self) -> []:
        list_client =[]
        client1 = Client('Santino', '32123543', '1234', 'Sarmiento 321', 'santino@gmail.com')
        client1.name
        client1.code
        client1.dni
        client1.address
        client1.email
        list_client.append()
        return list_client"""
        