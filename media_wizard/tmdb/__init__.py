from .config import TMDB_CLIENT, TMDBConfig, get_tmdb_client
from .tmdb_client import TMDBClient

__all__ = ["TMDBConfig", "TMDBClient", "TMDB_CLIENT", "get_tmdb_client"]


def init_app(app):
    tmdb_config = TMDBConfig.from_config(app.config, override_from_env=True)
    app.config[TMDB_CLIENT] = TMDBClient(tmdb_config)
    return app
