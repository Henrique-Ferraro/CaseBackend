from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
# from flask_bcrypt import Bcrypt

csrf = CSRFProtect()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    csrf . init_app ( 'caseBackend' )
    db . init_app (app)

# bcrypt = Bcrypt(app)

from views.view_cadastro import *
# from views.view_user import *

if __name__ == '__main__':
    app.run(debug=True)