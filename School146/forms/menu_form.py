from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class MenuForm(FlaskForm):
    product = StringField('Товар', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')