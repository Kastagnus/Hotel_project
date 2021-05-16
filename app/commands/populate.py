from flask_script import Command
from werkzeug.security import generate_password_hash
from app.models import db
from app.models.user import User, Roles, UserRoles
# from app.models.admin_roles import Roles, UserRoles
from app.models.hotel import Hotel

class Populate(Command):

    def run(self):
        init_db()

def init_db():
    # db.drop_all()
    # db.create_all()
    populate_db()
    # role = UserRoles.query.filter_by(role_id="1").first()
    # print(type(role.company.company_name))



def populate_db():
    # add_user()
    add_role()
    add_user_role()

def add_user():

    user1 = {
        "email": "email@email.com",
        "company_name": "geonik",
        "tax_id": "123456",
        "name": "ucha",
        "last_name": "khmaladze",
        "password": generate_password_hash("paroli123"),
    }
    user2 = {
        "email": "user@email.com",
        "company_name": "geonik12",
        "tax_id": "12345678",
        "name": "ucha",
        "last_name": "khmaladze",
        "password": "paroli123",
    }

    user1 = User(**user1)
    # user2 = User(**user2)
    user1.add(user1)
    # user1.add(user2)

def add_role():
    role = {
        "name":"Admin"
    }
    role = Roles(**role)
    db.session.add(role)
    db.session.commit()

def add_user_role():

    user = User.query.filter_by(name="ucha").all()
    role = Roles.query.filter_by(name="Admin").all()

    for user in user:
        user.role.extend(role)

    db.session.commit()
