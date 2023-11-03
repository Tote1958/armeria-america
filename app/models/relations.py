from app import db

clients_roles = db.Table('clients_roles', db.Column('client_id', db.Integer, db.ForeignKey('clients.id', primary_key=True)), db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True))
