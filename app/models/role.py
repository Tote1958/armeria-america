from app.config.database import db
from dataclasses import dataclass
from app.models.relations import clients_roles


@dataclass
class Role(db.Model):
    __tablename__ = 'roles'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String(250))
    __description = db.Column('description', db.String(250))
    clients = db.relationship('Client', secondary='clients_roles', back_populates="roles")
