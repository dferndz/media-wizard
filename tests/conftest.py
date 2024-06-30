import sys
import pytest

from media_wizard import create_app
from media_wizard.admin.commands import populate_db
from media_wizard.db.database import db


@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        db.create_all(app=app)
        yield app
        db.drop_all(app=app)
