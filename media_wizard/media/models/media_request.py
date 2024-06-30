from sqlalchemy_serializer import SerializerMixin

from media_wizard.db import db


class MediaRequest(db.Model, SerializerMixin):  # type: ignore
    request_id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.String(255))
    request_type = db.Column(db.String(140))
    name = db.Column(db.Text)
    seasons = db.relationship(
        "TVRequestSeason",
        back_populates="media_request",
        lazy=True,
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"{self.name} (type: {self.request_type}, tmdb id: {self.tmdb_id})"
        )


class TVRequestSeason(db.Model, SerializerMixin):  # type: ignore
    serialize_rules = ("-media_request",)

    season_request_id = db.Column(db.Integer, primary_key=True)
    media_request_id = db.Column(
        db.Integer, db.ForeignKey("media_request.request_id")
    )
    media_request = db.relationship(
        "MediaRequest", back_populates="seasons", lazy=True, single_parent=True
    )
    season_number = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Season {self.season_number}"
