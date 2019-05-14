from flask import Flask
from flask import redirect
from flask import url_for


from routes.todo import main as todo_routes
from routes.index import main as index_routes

app = Flask(__name__)


app.secret_key = 'random string'


app.register_blueprint(todo_routes, url_prefix='/todo')
app.register_blueprint(index_routes)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)