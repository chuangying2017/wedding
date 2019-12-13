from . import api
from flask import request, render_template


@api.route('/login')
def login():
    return render_template('login.html')
