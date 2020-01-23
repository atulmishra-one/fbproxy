from flask import Blueprint
from flask import request
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import jsonify
from flask import abort
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from app.plugins import login_manager

from app.models import User
from app.forms import LoginForm, RegisterUserForm
from app.plugins import db

app_views = Blueprint('views', __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app_views.route("login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter(User.email == form.email.data,
                                 User.password == bytes(form.password.data, encoding='utf-8'))\
            .first()
        if form.validate_on_submit() and user.is_active:
            login_user(user)
            return redirect(url_for("views.dashboard"))
        flash(form.errors, 'error')
        return redirect(url_for('views.login'))
    context = {
        'form': form
    }
    return render_template("views/login.html", **context)


@app_views.route("logout")
def logout():
    logout_user()
    return redirect(url_for("views.index"))


@app_views.route("forgot_password")
def forgot_password():
    return


@app_views.route("register", methods=['GET', 'POST'])
def register():
    form = RegisterUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.password.data != form.confirm_password.data:
                flash("Password does not match.", "error")
                return redirect(url_for("views.register"))
            user = User.query.filter(User.email == form.email.data).first()
            if user:
                flash("Email already taken.", "error")
                return redirect(url_for("views.register"))
            new_user = User(email=form.email.data, password=bytes(form.password.data, encoding='utf-8'))
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful.", "success")
            return redirect(url_for("views.register"))

        flash(form.errors, "error")
        return redirect(url_for("views.register"))
    context = {
        'form': form
    }
    return render_template("views/register.html", **context)


@app_views.route('')
def index():
    context = {}
    return render_template("views/index.html", **context)


@app_views.route("dashboard")
@login_required
def dashboard():
    context = {}
    return render_template("views/dashboard.html", **context)
