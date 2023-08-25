

class Supplier(db.Model):
    __name__= 'users'
    __cuil=''
    __email=''
    __code=''

    @property #seria como get name, agrega funcionalidad mas a un metodo
    def code(self)->str:
        return self.__code
    
    @code.setter #seria como set name, el arroba es un decorador, un patron de diseño
    def code (self, code:str):
        self.__code = code
    
    
    @property
    def name(self)->str:
        return self.__name__
    
    @name.setter
    def code (self, name:str):
        self.__name = name


    @property
    def cuil(self)->str:
        return self.__cuil
    
    @cuil.setter
    def cuil (self, cuil:str):
        self.__cuil = cuil

    
    @property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email (self, email:str):
        self.__email = email


    def __repr__(self) -> str: #  despues de -> es el tipo de dato que devuelve
        return f'Supplier: \n Nombre:{self.name}, \n Cuil:{self.cuil}, \n Email:{self.email}, \n Codigo:{self.code}'
    
    def __eq__(self,__value:object) -> bool: #comparamos si dos objetos son iguales
        return self.codigo == __value.code and self.name == __value.name