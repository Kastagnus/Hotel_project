from werkzeug.security import check_password_hash
from app.models import db
from flask_login import LoginManager, UserMixin
login_manager = LoginManager()

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    company_name = db.Column(db.String, nullable=False, unique=True)
    tax_id = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String, nullable=False)
    hotel = db.relationship("Hotel", backref="company")
    role = db.relationship("Roles", secondary="user_roles", backref="company")

    def check_password(self, password):
        return check_password_hash(self.password,password)

    @classmethod
    def read(cls,email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user

    def add(self, user):

        db.session.add(user)
        db.session.commit()

    def has_role(self, status):
        for role in self.role:
            if role.name == status:
                return True

class Roles(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String, unique=True)


class UserRoles(db.Model):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id", ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey("roles.id", ondelete='CASCADE'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))