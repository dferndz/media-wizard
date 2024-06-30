import logging

from media_wizard.media.resources import (
    MediaRequestItemResource,
    MediaRequestResource,
)
from media_wizard.rest import api


def init_app(app):
    logging.basicConfig(level=logging.INFO)
    api.add_resource(MediaRequestResource, "/media/request")
    api.add_resource(
        MediaRequestItemResource, "/media/request/<int:media_request_id>"
    )
    return app
