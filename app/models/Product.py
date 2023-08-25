from .. import db

class Product(db.Model):
    __tablename__ = 'products'
    __id = db.Column('id' , db.Integer, primary_key=True)
    __name = db.Column('name' , db.String(250))
    __caliber = db.Column('caliber', db.String(250))
    __brand = db.Column('brand', db.String(250))
    __description = db.Column('description'. db.String(250))
    __type = db.Column('type', db.String(250))
    __serial_number = db.Column('serial_number', db.String(250))

    @property # Es un decorador, hace un patron de diseño, le agrega funcionalidad al método en este caso, lo encapsula en un atributo, puede estar arriba de una clase o arriba de 
    def name(self)->str: # Sería el get name
        return self.__name
    
    @name.setter  # Sería el set name
    def name(self, value:str):
        self.__name = value

    @property
    def caliber(self)->str: # Sería el get caliber
        return self.__caliber
    
    @caliber.setter  # Sería el set caliber
    def caliber(self, value:str):
        self.__caliber = value
    
    @property
    def brand(self)->str: # Sería el get brand
        return self.__brand
    
    @brand.setter  # Sería el set brand
    def brand(self, value:str):
        self.__brand = value

    @property
    def description(self)->str: # Sería el get description
        return self.__description
    
    @description.setter  # Sería el set description
    def description(self, value:str):
        self.__description = value
    
    @property
    def type(self)->str: # Sería el get type
        return self.__type
    
    @type.setter  # Sería el set type
    def type(self, value:str):
        self.__type = value
    
    @property
    def serial_number(self)->str: # Sería el get serial number
        return self.__serial_number
    
    @serial_number.setter  # Sería el set serial number
    def serial_number(self, value:str):
        self.__serial_number = value

    def __repr__(self) -> str:  # Da la info de cada objeto
        return f'Product: \n Nombre: {self.name} \n Calibre: {self.caliber} \n Marca: {self.brand} \n Descripción: {self.description} \n Tipo: {self.type} \n Número de Serie: {self.serial_number}'    

    def __eq__(self, value: object) -> bool: # Es para comparar si dos objetos están en la BD
        return self.serial_number == value.serial_number