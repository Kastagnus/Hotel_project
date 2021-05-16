from flask import render_template, flash, Blueprint, redirect,url_for
from app.models.hotel import Hotel
from flask_login import current_user
from app.manage_property.forms import ManageForm

manage_blueprint = Blueprint("manage_property",
                             __name__,
                             template_folder="templates/manage_property")


@manage_blueprint.route("/manage", methods=["GET", "POST"])
def manage_property():
    form = ManageForm()

    if form.validate_on_submit():
        hotel = Hotel.query.filter_by(user_id=current_user.id).first()
        hotel_name = form.hotel_name.data
        address = form.address.data
        room_quantity = form.room_quantity.data
        stars = form.stars.data
        if hotel_name:
            hotel.hotel_name = hotel_name
            Hotel.update()
        if address:
            hotel.address = address
            Hotel.update()
        if room_quantity:
            hotel.room_quantity = room_quantity
            Hotel.update()
        if stars:
            hotel.stars = stars
            Hotel.update()
        # old_info = [hotel.hotel_name, hotel.address, hotel.room_quantity, hotel.stars]
        # new_info = [hotel_name, address, room_quantity, stars]
        # for item in new_info:
        #     if item:
        #         old_info[new_info.index(item)] = item
        #         Hotel.update()
        #         print(old_info[new_info.index(item)])


        flash("Item(s) updated successfully")
        return redirect(url_for("manage_property.manage_property"))

    return render_template("manage_property.html", form=form)
