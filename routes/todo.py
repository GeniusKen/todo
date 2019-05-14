from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    Blueprint,
    session,
)

from utils import format_time
from models.todo import Todo
from routes.index import main as index_main
import time

main = Blueprint('todo', __name__)


@main.route('/')
def index():
    u = session.get('user_name', None)
    if u is None:
        return redirect('/')
    todo_list = Todo.find_all(username = u)
    return render_template('todo_index.html', todos=todo_list,username = u)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Todo.new(form)
    t.username = session.get('user_name',None)
    t.ut = format_time(t.ut)
    t.save()
    return redirect(url_for('todo.index'))


@main.route('/delete/<int:todo_id>/')
def delete(todo_id):
    t = Todo.delete(todo_id)
    return redirect(url_for('.index'))


@main.route("/logout", methods=['get'])
def logout():
    session.pop("user_name")
    return redirect('/')


@main.route('/completed/<int:todo_id>/')
def completed(todo_id):
    t = Todo.complete(todo_id)
    return redirect(url_for('.index'))