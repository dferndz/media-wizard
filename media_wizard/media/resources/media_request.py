from typing import Any
from flask import jsonify
from flask_restful import Resource, reqparse
from media_wizard.db.database import db

from media_wizard.media.models import MediaRequest


class MediaRequestResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self, *args: Any, **kwds: Any) -> Any:
        super(*args, **kwds)
        self.parser.add_argument("media_id", type=str, required=True)
        self.parser.add_argument("request_type", type=str, required=True)

    def get(self):
        media_requests = MediaRequest.query.all() or []
        return jsonify(
            {"media_requests": [media_request.to_dict() for media_request in media_requests]}
        )
    
    def post(self):
        args = self.parser.parse_args()
        media_id = args["media_id"]
        request_type = args["request_type"]
        media_request = MediaRequest(media_id=media_id, request_type=request_type)
        db.session.add(media_request)
        db.session.commit()
        return jsonify(media_request.to_dict())