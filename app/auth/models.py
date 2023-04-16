import mongoengine as db
from flask_login import UserMixin

class User(db.Document, UserMixin):

    meta = {'collection': 'users', 'strict': False}
    username = db.StringField(max_length=20)
    password = db.StringField()
    authenticated = db.BooleanField(default=False)
    is_active = db.BooleanField(default=True)
    roles = db.ListField(db.StringField(), default=['AI'])
    delegation = db.StringField()
    numero = db.StringField()

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_role(self):
        return self.roles


# @login_manager.user_loader
# def user_loader(username):
#     return User.objects(username=username).first()