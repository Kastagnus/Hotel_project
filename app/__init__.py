import os
from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
from flask_login import logout_user, login_required
from app.models import db
from app.admin.admin import admin
from app.models.user import login_manager

basedir = os.path.abspath(os.path.dirname(__file__))
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "NEVERSAYITOUTLOUD"
    app.config["CSRF_ENABLED"] = True
    app.config["USER_ENABLE_EMAIL"] = False

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    admin.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
    login_manager.login_view = "login.login"
    from app.registration.views import registration_blueprint
    from app.login.views import login_blueprint
    from app.add_property.views import add_property_blueprint
    from app.dashboard.views import dashboard_blueprint
    from app.property.views import property_blueprint
    from app.manage_property.views import manage_blueprint
    app.register_blueprint(registration_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(add_property_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(property_blueprint)
    app.register_blueprint(manage_blueprint)

    @app.route("/")
    @app.route("/home")
    def home():
        return render_template("main.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("login.login"))

    return app
