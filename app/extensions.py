from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from roles_required import not_ROLE

# from flask_session import Session

db = MongoEngine()
# intialize bcrypt
bcrypt = Bcrypt()

LoginManager.not_ROLE = not_ROLE
login_manager = LoginManager()
