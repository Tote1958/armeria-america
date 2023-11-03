from app import db
from app.models.role import Role


class RoleRepository:

    def create(self, role: Role):
        db.session.add(role)
        db.commit()
        return role

