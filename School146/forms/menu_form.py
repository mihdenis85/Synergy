from flask_wtf import FlaskForm
from sqlalchemy import Column, String, Float
from wtforms import SubmitField
from wtforms.validators import DataRequired


class MenuForm(FlaskForm):
    product = Column(String, validators=[DataRequired()])
    price = Column(Float, validators=[DataRequired()])
    submit = SubmitField('Подтвердить')