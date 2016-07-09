from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
Bootstrap(app)

# import views to be registered
import csa.views

# import models to be registered
import csa.models
