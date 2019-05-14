from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
)

from models.user import User


main = Blueprint('index', __name__)


def current_user():
    uname = session.get('user_name',None)
    u = User.find_by(username=uname)
    return u


@main.route("/")
def index():
    u = session.get('user_name',None)
    template = render_template("index.html", user=u)
    r = make_response(template)
    r.set_cookie('cookie_name', 'TODO')
    return r

@main.route("/register", methods=['POST'])
def register():
    form = request.form
    u = User.register(form)
    return redirect(url_for('.index'))


@main.route("/login", methods=['POST'])
def login():
    form = request.form
    u = User.validate_login(form)
    if u is None:
        return redirect(url_for('.index'))
    else:
        session['user_name'] = u.username
        session.permanent = True
        return redirect(url_for('todo.index'))


@main.route("/logout", methods=['get'])
def logout():
    session.pop("user_name")
    return redirect(url_for(".index"))