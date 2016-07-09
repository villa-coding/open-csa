# from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from csa.models import User
from flask_wtf import Form
from wtforms import SubmitField
from wtforms.validators import DataRequired

UserForm = model_form(User, base_class=Form)
UserForm.submit = SubmitField()
