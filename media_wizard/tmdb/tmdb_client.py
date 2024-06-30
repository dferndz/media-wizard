import requests


class TMDBClient:
    media_types = {"tv", "movie"}

    def __init__(self, config) -> None:
        self.base_url = config.base_url
        self.api_key = config.api_key

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params={"api_key": self.api_key})
        return response.json()

    def get_media(self, tmdb_id, media_type):
        if media_type not in self.media_types:
            raise ValueError(f"Invalid media type: {media_type}")
        return self.get(f"{media_type}/{tmdb_id}")
