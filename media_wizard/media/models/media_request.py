from sqlalchemy_serializer import SerializerMixin
from media_wizard.db import db


class MediaRequest(db.Model, SerializerMixin):
    request_id = db.Column(db.Integer, primary_key=True)
    media_id = db.Column(db.String(255))
    request_type = db.Column(db.String(140))