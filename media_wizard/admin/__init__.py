from .admin import init_app as admin_init_app
from .auth import init_app as auth_init_app
from .commands import init_app as commands_init_app


def init_app(app):
    admin_init_app(app)
    auth_init_app(app)
    commands_init_app(app)
    return app
