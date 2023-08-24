class Product_type:
    __tablename__ = 'product_type'
    __name__ = ''
    __code__ = ''
    __description__ = ''

# Property permite que el método sea llamado como un atributo
    @property 
    def name(self) -> str:
        return self.__name__
    @name.setter
    def name(self, name: str):
        self.__name__ = name

    @property
    def code(self) -> str:
        return self.__code__
    @code.setter
    def code(self, code: str):
        self.__code__ = code

    @property
    def description(self) -> str:
        return self.__description__
    @description.setter
    def description(self, description: str):
        self.__description__ = description

#repr sirve para representar el objeto como un string
    def __repr__(self) -> str:
        return f'Product_type:[name: {self.__name__}, code: {self.__code__}, description: {self.__description__}]'
#eq sirve para comparar dos objetos
    def __eq__(self, o: object) -> bool:
        return self.__name__ == o.name and self.__code__ == o.code and self.__description__ == o.description