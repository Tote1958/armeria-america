from app.config.database import db


class Product_type(db.Model):
    __tablename__ = 'product_type'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String(250))
    __code = db.Column('code', db.String(250))
    __description = db.Column('description', db.String(250)) 

# Property permite que el método sea llamado como un atributo
    @property 
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code
    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
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