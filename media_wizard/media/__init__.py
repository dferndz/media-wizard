from media_wizard.rest import api
from media_wizard.media.resources import MediaRequestResource


def init_app(app):
    api.add_resource(MediaRequestResource, "/media/request")
    return app