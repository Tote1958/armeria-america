from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property

class Brand(db.Model):
    __tablename__ = 'brands'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String(250))
    __origin = db.Column('name', db.String(250))



    """name: str name of the brand max char 100
       origin: str origin of the brand max char 100  """
    def __init__(self, name:str, origin:str):
        self.__name = name
        self.__origin = origin

    @hybrid_property  #Funciona como un get id
    def id(self)->int:
        return self.__id
    
    @id.setter #Funciona como un set id
    def id(self, id:str): 
        self.__id = id
    
    @hybrid_property #Funciona como un get
    def name(self)->str:
        return self.__name
    
    @name.setter #Funciona como un set id
    def name(self, name:str):
        self.__name = name
    
    @hybrid_property #Funciona como un get 
    def origin(self)->str:
        return self.__origin
    
    @origin.setter #Funciona como un set id
    def origin(self, origin:str):
        self.__origin = origin
    
    def __repr__(self) -> str: #Da la informacion de un objeto
        return f'Name: {self.__name},\nOrigin: {self.__origin}'
    
    def __eq__(self, value:object) -> bool: #Es para comparar si dos objetos estan en la BD
        return self.dni == value.dni
    
    
