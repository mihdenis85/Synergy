from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class EditUserForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль')
    submit = SubmitField('Изменить')