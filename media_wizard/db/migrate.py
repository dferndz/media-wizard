from flask_migrate import Migrate

from media_wizard.db.database import db

db_migrate = Migrate()


def migrate(app):
    db_migrate.init_app(app, db)
    return app
