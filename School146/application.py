import os
from datetime import timedelta

from flask import Flask, render_template, url_for, request
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from werkzeug.utils import redirect, secure_filename

from School146.data import db_session
from School146.data.models import Article
from School146.data.models.users import User
from School146.forms import RegisterForm, LoginForm, ArticleForm

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
UPLOAD_FOLDER = '/users_photo'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key_jwkjldjwkdjlkwdkwjdldwhifwifhwiuhiuefhwiufhiuehf0f9wwefw'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db = db_session.create_session()
    user = db.query(User).get(user_id)
    return user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    if form.password.data and form.name.data and form.email.data and form.password_again.data:
        if form.validate_on_submit():
            if len(form.password.data) < 6:
                return render_template('register.html',
                                       form=form,
                                       message="Пароль должен содержать не меньше 6 символов")
            if form.password.data.isdigit() or form.password.data.isalpha():
                return render_template('register.html',
                                       form=form,
                                       message="Пароль должен состоять не только из букв или цифр")
            if form.password_again.data != form.password.data:
                return render_template('register.html', form=form, message="Пароли не совпадают")
            if not form.name.data or not form.email.data:
                return render_template('register.html', form=form,
                                       message='Проверьте правильность заполнения полей')
            db = db_session.create_session()
            if db.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html',
                                       form=form,
                                       message="Такой пользователь уже существует")
            user = User(
                name=form.name.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db.add(user)
            db.commit()
            login_user(user, remember=True)
            db.close()
            return redirect('/')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    login_form = LoginForm()
    if login_form.validate_on_submit():
        db = db_session.create_session()
        user = db.query(User).filter(User.email == login_form.email.data).first()
        if not user:
            db.close()
            return render_template('login.html', form=login_form, message="Такого пользователя не существует")
        if user.check_password(login_form.password.data):
            login_user(user, remember=True)
            db.close()
            return redirect('/')
        else:
            db.close()
            return render_template('login.html', form=login_form, message="Неправильный пароль")
    return render_template('login.html', form=login_form)


@app.route('/add_article', methods=['GET', 'POST'])
@login_required
def add_article():
    form = ArticleForm()
    if form.validate_on_submit():
        assets_dir = os.path.join(
            os.path.dirname(app.instance_path), 'School146/assets'
        )
        db = db_session.create_session()
        article = Article()
        article.title = form.title.data
        article.text = form.text.data
        if form.picture.data:
            f = form.picture.data

            filename = secure_filename(f.filename)
            article.picture = str(os.path.join('School146/assets', filename))
            f.save(os.path.join(assets_dir, filename))

        db.add(article)
        db.commit()
        db.close()
        return redirect('/')
    return render_template('add_article.html', form=form)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_file(request):
    pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


from os import path
db_session.global_init(path.join(path.dirname(__file__), './db/project.db'))

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)