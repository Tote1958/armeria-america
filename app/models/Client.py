from app.config.database import db

class Client(db.Model):
    __tablename__ = 'clients'
    __id = db.Column(db.Integer, primary_key=True)
    __name = db.Column(db.String(250))
    __dni = db.Column(db.String(250))
    __client_code = db.Column(db.String(250))
    __address = db.Column(db.String(250))
    __email = db.Column(db.String(250))

    @property
    def client_code(self)->str:
        return self.__client_code
    
    @client_code.setter
    def client_code(self, code:str):
        self.__client_code = code
    
    @property
    def name(self)->str:
        return self.__name
    
    @client_code.setter
    def name(self, name:str):
        self.__name = name
    
    @property
    def dni(self)->str:
        return self.__dni
    
    @client_code.setter
    def dni(self, dni:str):
        self.__dni = dni
    
    @property
    def address(self)->str:
        return self.__address
    
    @address.setter
    def address(self, address:str):
        self.__address = address

    @property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email(self, email:str):
        self.__email = email
    
    def __repr__(self) -> str:
        return f'Name: {self.__name},\nDNI: {self.__dni},\nCodigo de cliente: {self.__client_code},\nDireccion: {self.__address},\nEmail: {self.__email}'
    
    def __eq__(self, value:object) -> bool:
        return self.dni == value.dni