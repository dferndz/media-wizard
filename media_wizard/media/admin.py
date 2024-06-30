from flask_admin.contrib import sqla


class MediaRequestAdmin(sqla.ModelView):
    column_list = ["request_id", "name", "tmdb_id", "request_type", "seasons"]
    can_edit = True


class TVRequestSeasonAdmin(sqla.ModelView):
    column_list = ["season_request_id", "media_request", "season_number"]
    can_edit = True
