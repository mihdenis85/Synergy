import os
from datetime import timedelta

from flask import Flask, render_template
from flask_login import LoginManager

from School146.data import db_session
from School146.data.models.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key_jwkjldjwkdjlkwdkwjdldwhifwifhwiuhiuefhwiufhiuehf0f9wwefw'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)

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



from os import path
db_session.global_init(path.join(path.dirname(__file__), './db/project.db'))

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)