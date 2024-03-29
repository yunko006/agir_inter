from functools import wraps
from flask_login import current_user
from flask_login.config import EXEMPT_METHODS, USE_SESSION_FOR_NEXT
from flask_login.utils import (
    expand_login_view,
    make_next_param,
    login_url as make_login_url,
)
from flask import current_app, session, request, redirect


def AI_required(func):
    @wraps(func)
    def decorated_views(*args, **kwargs):
        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get("LOGIN_DISABLED"):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        # elif not current_user.is_anonymous:
        #     return current_app.login_manager.unauthorized()
        elif "Admin" in current_user.roles:
            return func(*args, **kwargs)
        elif "AI" not in current_user.roles:
            return current_app.login_manager.not_ROLE()

        return func(*args, **kwargs)

    return decorated_views


def benevole_required(func):
    @wraps(func)
    def decorated_views(*args, **kwargs):
        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get("LOGIN_DISABLED"):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif "Admin" in current_user.roles:
            return func(*args, **kwargs)
        elif "benevole" not in current_user.roles:
            return current_app.login_manager.not_ROLE()
        return func(*args, **kwargs)

    return decorated_views


def admin_required(func):
    @wraps(func)
    def decorated_views(*args, **kwargs):
        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get("LOGIN_DISABLED"):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_anonymous:
            return current_app.login_manager.unauthorized()
        elif "Admin" not in current_user.roles:
            return current_app.login_manager.not_ROLE()
        return func(*args, **kwargs)

    return decorated_views


def not_ROLE(self):
    # This method of LoginManager requires that you provide a `not_ROLE_view` attribute to LoginManager.
    # `not_ROLE_view` can be provided where you provide a `login_view` for unauthorized users.
    not_ROLE_view = self.not_ROLE_view
    config = current_app.config
    if config.get("USE_SESSION_FOR_NEXT", USE_SESSION_FOR_NEXT):
        not_ROLE_url = expand_login_view(not_ROLE_view)
        session["_id"] = self._session_identifier_generator()
        session["next"] = make_next_param(not_ROLE_url, request.url)
        redirect_url = make_login_url(not_ROLE_view)
    else:
        redirect_url = make_login_url(not_ROLE_view, next_url=request.url)
    return redirect(redirect_url)


# code source : https://github.com/schwartz721/role_required
