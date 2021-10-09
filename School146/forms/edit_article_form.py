import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, regexp


class EditArticleForm(FlaskForm):
    title = StringField('Изменить название статьи', validators=[DataRequired()])
    text = TextAreaField('Изменить текст статьи', validators=[DataRequired()])
    picture = FileField('Изменить картинку', validators=[FileAllowed(['jpg', 'png'],
                                                            'Допустимы только изображения форматов jpg и png')])
    submit = SubmitField('Подтвердить изменения')