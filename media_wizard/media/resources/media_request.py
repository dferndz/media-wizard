from typing import Any

from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from media_wizard.db.database import db
from media_wizard.media.models import MediaRequest
from media_wizard.media.models.media_request import TVRequestSeason
from media_wizard.tmdb import get_tmdb_client


class MediaRequestItemResource(Resource):
    def get(self, media_request_id):
        tmdb = get_tmdb_client()
        media_request = MediaRequest.query.get(media_request_id)
        tmdb_media = tmdb.get_media(
            media_request.tmdb_id, media_request.request_type
        )
        return jsonify(
            {"media_request": media_request.to_dict(), "tmdb": tmdb_media}
        )


class MediaRequestResource(Resource):
    parser = reqparse.RequestParser()

    def __init__(self, *args: Any, **kwds: Any):
        super(*args, **kwds)
        self.parser.add_argument("tmdb_id", type=str, required=True)
        self.parser.add_argument("request_type", type=str, required=True)
        self.parser.add_argument("seasons", action="append", required=False)

    def get(self):
        media_requests = MediaRequest.query.all() or []
        return jsonify(
            {
                "media_requests": [
                    media_request.to_dict() for media_request in media_requests
                ]
            }
        )

    def post(self):
        args = self.parser.parse_args()
        tmdb_id = args["tmdb_id"]
        request_type = args["request_type"]
        seasons = (
            [int(s) for s in args["seasons"]]
            if args["seasons"]
            and len(args["seasons"]) > 0
            and args["seasons"][0]
            else []
        )

        # Check if a request already exists for this tmdb_id
        existing_request = MediaRequest.query.filter_by(
            tmdb_id=tmdb_id
        ).first()
        if existing_request is not None and request_type == "movie":
            return jsonify(existing_request.to_dict())

        tmdb_media = self.tmdb.get_media(tmdb_id, request_type)
        tmdb_name = tmdb_media.get("name") or tmdb_media.get("title")
        tmdb_season_list = tmdb_media.get("seasons", [])
        tmdb_seasons = dict(
            {season["season_number"]: season for season in tmdb_season_list}
        )

        if tmdb_name is None:
            return jsonify({"error": "Invalid tmdb_id"}), 400

        if request_type == "tv" and seasons:
            for season_number in seasons:
                if season_number not in tmdb_seasons:
                    return make_response(
                        jsonify(
                            {
                                "error": f"Invalid season number: {season_number}"  # noqa
                            }
                        ),
                        400,
                    )

        media_request = (
            MediaRequest(
                tmdb_id=tmdb_id, request_type=request_type, name=tmdb_name
            )
            if existing_request is None
            else existing_request
        )

        if request_type == "tv":
            for season_number in seasons:
                # check if request for season exists
                existing_season = TVRequestSeason.query.filter_by(
                    media_request_id=media_request.request_id,
                    season_number=season_number,
                ).first()
                if existing_season is None:
                    media_request.seasons.append(
                        TVRequestSeason(season_number=season_number)
                    )

        db.session.add(media_request)
        db.session.commit()
        return jsonify(media_request.to_dict())

    @property
    def tmdb(self):
        return get_tmdb_client()
