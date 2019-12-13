from flask import Flask, render_template, request, escape, url_for
from wed import api as api_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix="/auth")


@app.route('/')
def hello_world():
    return 'Hello World!!'


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
