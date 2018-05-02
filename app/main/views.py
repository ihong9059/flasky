from flask import render_template
from . import main
from flask_login import login_user, logout_user, login_required, \
    current_user


@main.route('/')
def index():
    return render_template('index.html')
