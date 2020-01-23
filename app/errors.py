from flask import current_app
from werkzeug import exceptions
from flask import render_template
from sqlalchemy.exc import SQLAlchemyError
from flask import flash
from flask import redirect
from flask import url_for


@current_app.errorhandler(exceptions.NotFound)
def handle_not_found(e):
    return render_template("errors/404.html", e=e), 404


@current_app.errorhandler(exceptions.InternalServerError)
def handle_internal_error(e):
    return render_template("errors/500.html", e=e), 500


@current_app.errorhandler(SQLAlchemyError)
def handle_sql_error(e):
    current_app.logger.error(e)
    return render_template("errors/500.html", e="Database Error"), 500


@current_app.errorhandler(401)
def handle_auth_error(e):
    current_app.logger.error(e)
    flash("Please login.", "error")
    return redirect(url_for("views.login"))
