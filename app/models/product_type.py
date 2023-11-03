from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property


class ProductType(db.Model):
    __tablename__ = 'product_type' 
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True) # db.Integer es un tipo de dato de SQL, un numero autoincrementable
    __name = db.Column('name', db.String(250))
    __code = db.Column('code', db.String(250))
    __description = db.Column('description', db.String(250)) 

#constructor
    '''Parametro name: (str) name of the product type, max 250 characters
       Parametro code: (str) code of the product type, max 250 characters
       Parametro description: (str) description of the product type, max 250 characters'''
    def __init__(self, name: str, code: str, description: str):
        self.__name = name 
        self.__code = code
        self.__description = description

# hybrid_property sirve para que se pueda acceder a los atributos privados
    @hybrid_property
    def id(self) -> int:
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id
    
    @hybrid_property 
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @hybrid_property
    def code(self) -> str:
        return self.__code
    @code.setter
    def code(self, code: str):
        self.__code = code

    @hybrid_property
    def description(self) -> str:
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

#repr sirve para representar el objeto como un string
    def __repr__(self) -> str:
        return f'Product_type:[name: {self.__name}, code: {self.__code}, description: {self.__description}]'
#eq sirve para comparar dos objetos
    def __eq__(self, o: object) -> bool:
        return self.name == o.name and self.code == o.code and self.description == o.description