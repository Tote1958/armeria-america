from abc import ABC, abstractmethod
from app.config.database import db

class CRUD(ABC):

    @abstractmethod
    def create(self, entity:db.Model):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id:int):
        pass

    @abstractmethod
    def update(self, entity:db.Model, id:int):
        pass

    @abstractmethod
    def delete(self, entity:db.Model):
        pass