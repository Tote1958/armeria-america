from .. import db

class Client(db.Model):
    __tablename__ = 'clients'

    __id = db.Column('id',)