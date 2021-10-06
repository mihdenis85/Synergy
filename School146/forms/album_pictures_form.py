from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired


class AlbumPictureForm(FlaskForm):
    title = StringField('Название картинки')
    album = SelectField('Альбом', )
    picture = FileField('Файл', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')