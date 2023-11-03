from app.config.database import db
from dataclasses import dataclass
from app.models.client import Base, association_table
@dataclass
class Role(db.Model, Base):
    __tablename__ = 'roles'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String(250))
    __description = db.Column('name', db.String(250))
    relationship = db.relationship(
        secondary=association_table, back_populates="role"
    )