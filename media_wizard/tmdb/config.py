import os

from flask import current_app

from .tmdb_client import TMDBClient

TMDB_API_URL = "TMDB_API_URL"
TMDB_API_KEY = "TMDB_API_KEY"
TMDB_CLIENT = "TMDB_CLIENT"


def get_tmdb_client() -> TMDBClient:
    return current_app.config.get(TMDB_CLIENT)  # type: ignore


class TMDBConfig:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    @classmethod
    def from_config(cls, config, override_from_env=False):
        if override_from_env:
            config[TMDB_API_URL] = os.getenv(
                TMDB_API_URL, config.get(TMDB_API_URL)
            )
            config[TMDB_API_KEY] = os.getenv(
                TMDB_API_KEY, config.get(TMDB_API_KEY)
            )
        return cls(
            base_url=config.get(TMDB_API_URL), api_key=config.get(TMDB_API_KEY)
        )
