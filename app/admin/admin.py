from flask import url_for, redirect, abort
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, AnonymousUserMixin
from app.admin import Admin
from app.models import db
from app.models.hotel import Hotel
from app.models.user import User
from flask_admin import AdminIndexView



class AdminModelView(ModelView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login.login'))



class MyAdminIndexView(AdminIndexView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        print(type(current_user))
        try:
            return current_user.has_role('Admin')
        except:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login.login'))


admin = Admin(name="Panel", template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(AdminModelView(User, db.session, name="Users", category='User Management'))
admin.add_view(AdminModelView(Hotel, db.session, name="Properties", category='Property Management'))
