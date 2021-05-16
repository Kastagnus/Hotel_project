from flask import Blueprint, redirect, render_template, url_for, flash
from app.registration.forms import RegistrationForm
from app.models.user import User
from werkzeug.security import generate_password_hash

registration_blueprint = Blueprint('register',
                                   __name__,
                                   template_folder="templates/registration")

@registration_blueprint.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        company_name = form.company_name.data
        tax_id = form.tax_id.data
        name = form.name.data
        last_name = form.last_name.data
        password = generate_password_hash(form.password.data)
        user = User(email=email,company_name=company_name,tax_id=tax_id,name=name,last_name=last_name,password=password)

        if User.read(email):
            flash(f"Sorry! Account with email {email} already exists")
        else:
            user.add(user)
            flash("You have been successfully registered")
            return redirect(url_for("login.login"))

    return render_template("registration.html",form=form)
