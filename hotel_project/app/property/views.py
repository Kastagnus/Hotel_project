from flask import Blueprint, render_template
from flask_login import current_user
from app.models.hotel import Hotel

property_blueprint = Blueprint("property",
                                __name__,
                                template_folder="templates/property")

@property_blueprint.route("/property", methods=["GET", "POST"])
def property():

    hotel = Hotel.query.filter_by(user_id=current_user.id).first()
    hotel_name = hotel.hotel_name
    address = hotel.address
    room_quantity = hotel.room_quantity
    stars = hotel.stars

    return render_template("property.html", hotel_name=hotel_name,address=address,room_quantity=room_quantity,stars=stars)