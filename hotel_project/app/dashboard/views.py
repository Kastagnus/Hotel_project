from flask import Blueprint, render_template
from flask_login import current_user

dashboard_blueprint = Blueprint("dashboard",
                                __name__,
                                template_folder="templates/dashboard")

@dashboard_blueprint.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    company_name = current_user.company_name
    tax_id = current_user.tax_id
    name = current_user.name
    last_name = current_user.last_name

    return render_template("dashboard.html", company_name=company_name,tax_id=tax_id,name=name,last_name=last_name)
