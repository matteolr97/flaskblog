from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class TravelForm (FlaskForm) :
    destination= SelectField('Destination', validators=[DataRequired()])

    budget = SelectField('Budget',
                        validators=[DataRequired()])
    duration = SelectField('Duration',
                        validators=[DataRequired()])
    participants = StringField('Participants',
                        validators=[DataRequired()])
    description = SelectField('Type of travel',
                        validators=[DataRequired()])
    submit = SubmitField('Create Travel')
