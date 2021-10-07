import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, regexp


class ArticleForm(FlaskForm):
    title = StringField('Название статьи', validators=[DataRequired()])
    text = TextAreaField('Текст статьи', validators=[DataRequired()])
    picture = FileField('Картинка', validators=[FileRequired(),
                                                FileAllowed(['jpg', 'png'],
                                                            'Допустимы только изображения форматов jpg и png')])
    submit = SubmitField('Подтвердить')