from app.login.forms import LoginForm
from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import login_user
from app.models.user import User
from app.models.hotel import Hotel
from flask_login import logout_user

login_blueprint = Blueprint("login",
                            __name__,
                            template_folder="templates\login")

@login_blueprint.route("/login", methods=["GET","POST"])
def login():
    logout_user()
    form = LoginForm()

    if form.validate_on_submit():
        user = User.read(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            # next = request.args.get("next")
            hotel = Hotel.query.filter_by(user_id=user.id).first()
            if hotel is None:
                return redirect(url_for("add_property.add_property"))
            else:
                return redirect(url_for("dashboard.dashboard"))

    return render_template("login.html", form=form)


