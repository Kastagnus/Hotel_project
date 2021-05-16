from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ManageForm(FlaskForm):

    hotel_name = StringField("Hotel name")
    address = StringField("Address")
    room_quantity = StringField("Number of rooms")
    stars = StringField("Number of stars")
    update = SubmitField("Update")