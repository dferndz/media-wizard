from media_wizard.media.resources import MediaRequestResource
from media_wizard.rest import api


def init_app(app):
    api.add_resource(MediaRequestResource, "/media/request")
    return app
