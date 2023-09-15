from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property

class Supplier(db.Model):
    __tablename__ ='supplier'
    __id = db.Column('id' , db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name' , db.String(250))
    __cuil= db.Column('cuil', db.String(250))
    __email= db.Column('email', db.String(250))
    __code= db.Column('code', db.String(250)) 

    """
    name: str name of supplier max char 250
    cuil: str cuil of supplier max char 250
    email: str email of supplier max char 250
    code: str code of supplier max char 250
    """
    
    def __init__(self, name:str, cuil:str, email:str, code:str): #Constructor(parametros)
        self.__name = name
        self.__cuil = cuil
        self.__email = email
        self.__code = code

    @hybrid_property
    def id(self)->int:
        return self.__id
    
    @id.setter
    def id(self, id:str):
        self.__id = id

    @hybrid_property #seria como get name, agrega funcionalidad mas a un metodo
    def code(self)->int: #ver si es int o str
        return self.__code
    
    @code.setter #seria como set name, el arroba es un decorador, un patron de diseño
    def code (self, code:str):
        self.__code = code
    
    
    @hybrid_property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def code (self, name:str):
        self.__name = name


    @hybrid_property
    def cuil(self)->str:
        return self.__cuil
    
    @cuil.setter
    def cuil (self, cuil:str):
        self.__cuil = cuil

    
    @hybrid_property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email (self, email:str):
        self.__email = email


    def __repr__(self) -> str: #  despues de -> es el tipo de dato que devuelve
        return f'Supplier: \n Nombre:{self.name}, \n Cuil:{self.cuil}, \n Email:{self.email}, \n Codigo:{self.code}'
    
    def __eq__(self,__value:object) -> bool: #comparamos si dos objetos son iguales
        return self.codigo == __value.code and self.name == __value.name
    