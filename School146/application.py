import os
from datetime import timedelta

from flask import Flask, render_template, url_for, request, jsonify
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_wtf import CSRFProtect
from werkzeug.utils import redirect, secure_filename

from School146.data import db_session
from School146.data.models import Article
from School146.data.models.users import User
from School146.forms import RegisterForm, LoginForm, ArticleForm, EditUserForm

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
UPLOAD_FOLDER = '/users_photo'

csrf = CSRFProtect()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key_jwkjldjwkdjlkwdkwjdldwhifwifhwiuhiuefhwiufhiuehf0f9wwefw'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024
csrf.init_app(app)

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
            return redirect('/user_info')
        else:
            db.close()
            return render_template('login.html', form=login_form, message="Неправильный пароль")
    return render_template('login.html', form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/add_article', methods=['GET', 'POST'])
@login_required
def add_article():
    form = ArticleForm()
    if form.validate_on_submit():
        assets_dir = os.path.join(
            os.path.dirname(app.instance_path), 'School146/static/user_img'
        )
        db = db_session.create_session()
        article = Article()
        article.title = form.title.data
        article.text = form.text.data
        if form.picture.data:
            f = form.picture.data
            filename = secure_filename(f.filename)
            article.picture = filename
            f.save(os.path.join(assets_dir, filename))
        else:
            db.close()
            return render_template('add_article.html', form=form, message='Картинка обязательна', add_edit="Добавление")

        db.add(article)
        db.commit()
        db.close()
        return redirect('/')
    return render_template('add_article.html', form=form, add_edit="Добавление")


@app.route('/article_info/<int:id>', methods=['GET', 'POST'])
def article_info(id):
    db = db_session.create_session()
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        return redirect(url_for('index'))
    db.close()
    if current_user.is_authenticated:
        editable = True
    else:
        editable = False
    return render_template('article_info.html', title=article.title, text=article.text, picture=article.picture,
                           editable=editable)


@app.route('/edit_user_info', methods=['GET', 'POST'])
@login_required
def edit_user_info():
    all_data = {
        'email': current_user.email,
        'name': current_user.name
    }
    form = EditUserForm(data=all_data)
    if form.validate_on_submit():
        db = db_session.create_session()
        password = form.password.data
        user_now = db.query(User).filter(User.id == current_user.id).first()
        if user_now.check_password(password):
            user_now.name = form.name.data
            emails = db.query(User).filter(User.email == form.email.data).all()
            if len(emails) >= 2 or (len(emails) == 1 and current_user.email != form.email.data):
                db.close()
                return render_template('edit_user_info.html', form=form,
                                       message="Такая почта уже используется в другом аккаунте")
            else:
                user_now.email = form.email.data
            db.commit()
            db.close()
            return redirect('/user_info')
        else:
            return render_template('edit_user_info.html', form=form, message="Неправильный пароль")
    return render_template('edit_user_info.html', form=form)


@app.route('/user_info')
@login_required
def user_info():
    return render_template('user_info.html')


@app.errorhandler(401)
def unauth(error):
    return redirect(url_for('index'))


from os import path
db_session.global_init(path.join(path.dirname(__file__), './db/project.db'))

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)