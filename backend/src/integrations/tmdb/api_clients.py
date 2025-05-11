from django.conf import settings


class TmdbApiClient:
    base_url = "https://api.themoviedb.org/3"
    api_key = settings.get("TMDB_API_KEY")
    api_read_access_token = settings.get("TMDB_API_READ_ACCESS_TOKEN")
