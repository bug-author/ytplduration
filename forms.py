from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Link(FlaskForm):
    # var > html reference, first arg > label/description
    link = StringField('Link', validators=[DataRequired()])
    search = SubmitField('Find Duration')
