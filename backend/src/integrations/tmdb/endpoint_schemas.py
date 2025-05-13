from pydantic import BaseModel, field_validator


class TmdbDiscoverFilm(BaseModel):
    id: int
    title: str
    original_title: str
    original_language: str
    release_date: str
    poster_path: str | None
    overview: str

    # TODO: We might want to use these fields in the future.
    popularity: float
    vote_average: float

    def to_django_model_defaults(self):
        return {
            "title": self.title,
            "original_title": self.original_title,
            "release_date": self.release_date or None,
            "synopsis": self.overview,
            "poster": self.poster_path,
            "has_synced_with_tmdb": True,
        }


class TmdbDiscoverFilmsPage(BaseModel):
    results: list[TmdbDiscoverFilm | dict]

    @field_validator("results", mode="before")
    def coerce_results(cls, value):
        if isinstance(value, list) and all(isinstance(v, dict) for v in value):
            return [TmdbDiscoverFilm(**v) for v in value]
        return value

    def process_page(self):
        from films.models import Film

        Film.objects.bulk_create(
            [
                Film(
                    tmdb_id=film.id,
                    **film.to_django_model_defaults(),
                )
                for film in self.results
            ],
            ignore_conflicts=True,
        )
