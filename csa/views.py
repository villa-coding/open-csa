from flask import render_template
from csa import app, db
from csa.models import User
from csa.forms import UserForm

@app.route("/")
def hello():
    user_form = UserForm()
    return render_template('index.html', form=user_form)
