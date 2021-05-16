from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email(message="Wrong format")])
    company_name = StringField("Company Name", validators=[DataRequired()])
    tax_id = StringField("Taxpayer ID", validators=[DataRequired()])
    name = StringField("Name of responsible person", validators=[DataRequired()])
    last_name = StringField("Last name of responsible person", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("rep_password")])
    rep_password = PasswordField("Repeat password", validators=[DataRequired()])
    register = SubmitField("Register")

