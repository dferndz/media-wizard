from sqlalchemy_serializer import SerializerMixin
from media_wizard.db import db


class User(db.Model, SerializerMixin):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
