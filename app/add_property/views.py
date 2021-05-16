from app.add_property.forms import HotelForm
from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user
from app.models.hotel import Hotel

add_property_blueprint = Blueprint("add_property",
                                   __name__,
                                   template_folder="templates/add_property")


@add_property_blueprint.route("/add_property", methods=["GET", "POST"])
def add_property():
    form = HotelForm()

    if form.validate_on_submit():
        hotel_name = form.hotel_name.data
        address = form.address.data
        room_quantity = form.room_quantity.data
        stars = form.stars.data
        user_id = current_user.id
        hotel = Hotel(hotel_name=hotel_name, address=address, room_quantity=room_quantity, stars=stars, user_id=user_id)
        hotel.add(hotel)
        return redirect(url_for("dashboard.dashboard"))
    return render_template("add_property.html", form=form)
