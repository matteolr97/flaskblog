from flask import render_template, request, Blueprint

travels = Blueprint('travels', __name__)


@travels.route("/travel")
def travel():
    return render_template('travel.html')