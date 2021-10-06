from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AlbumForm(FlaskForm):
    title = StringField('Название альбома', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')