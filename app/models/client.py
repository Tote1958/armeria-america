from __future__ import annotations
from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property
from dataclasses import dataclass
from app.models.relations import clients_roles

@dataclass
class Client(db.Model):
    __tablename__ = 'clients'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String(250))
    __dni = db.Column('dni', db.String(250))
    __code = db.Column('code', db.String(250)) 
    __address = db.Column('address', db.String(250))
    __email = db.Column('email', db.String(256))

    roles = db.relationship('Role', secondary='clients_roles', back_populates="client")



    """name: str name of client max char 50
       dni: alfanumerico  """
""" def __init__(self, name:str, dni:str, code:str, address:str, email:str):
        self.__name = name
        self.__dni = dni
        self.__code = code
        self.__address = address
        self.__email = email
    

    @hybrid_property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @hybrid_property
    def code(self) -> str:
        return self.__code
    
    @code.setter
    def code(self, code:str):
        self.__code = code
    
    @hybrid_property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self, name:str):
        self.__name = name
    
    @hybrid_property
    def dni(self)->str:
        return self.__dni
    
    @dni.setter
    def dni(self, dni:str):
        self.__dni = dni
    
    @hybrid_property
    def address(self)->str:
        return self.__address
    
    @address.setter
    def address(self, address:str):
        self.__address = address

    @hybrid_property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email(self, email:str):
        self.__email = email
    
    def __repr__(self) -> str:
        return f'Name: {self.__name},\nDNI: {self.__dni},\nCodigo de cliente: {self.__client_code},\nDireccion: {self.__address},\nEmail: {self.__email}'
    
    def __eq__(self, value:object) -> bool:
        return self.dni == value.dni
    """

