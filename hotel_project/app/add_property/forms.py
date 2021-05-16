from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HotelForm(FlaskForm):

    hotel_name = StringField("Hotel Name", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    room_quantity = StringField("Number of rooms", validators=[DataRequired()])
    stars = StringField("Number of stars", validators=[DataRequired()])
    add = SubmitField("Add property")