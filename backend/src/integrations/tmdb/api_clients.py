from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator

import pycountry
import requests
from django.conf import settings
from integrations.tmdb.rate_limiter import tmdb_rate_limit

if TYPE_CHECKING:
    from requests import Response


class TmdbApiClient:
    base_url = "https://api.themoviedb.org/3"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {settings.TMDB_READ_ACCESS_TOKEN}",
                "Accept": "application/json",
            }
        )

    @tmdb_rate_limit
    def request(
        self,
        method: str | bytes,
        endpoint: str,
        return_json: bool = True,
        raise_status_exception: bool = True,
        **kwargs,
    ) -> dict | Response:
        response = self.session.request(method, f"{self.base_url}{endpoint}", **kwargs)

        if raise_status_exception:
            response.raise_for_status()

        if return_json:
            return response.json()

        return response

    def exhaust_paginated_endpoint(
        self, *args, params: dict[str, str | int | bool], **kwargs
    ) -> Iterator[list[dict[str, Any]]]:
        page = 1
        total_pages = None

        while total_pages is None or page < total_pages:
            params["page"] = page
            response = self.request(*args, params=params, **kwargs)
            yield response["results"]

            total_pages = total_pages or response["total_pages"]

            if not total_pages or page >= total_pages:
                break

            page += 1

    def get_films(
        self, *, params: dict[str, str | int | bool] | None = None, **kwargs
    ) -> Iterator[list[dict[str, Any]]]:
        return self.exhaust_paginated_endpoint(
            "GET",
            "/discover/movie",
            params={
                **(params or {}),
                "include_adult": False,
                "include_video": False,
            },
            **kwargs,
        )

    def get_all_films(self) -> Iterator[list[dict[str, Any]]]:
        for country in pycountry.countries:
            for year in range(2000, 2024):
                yield from self.get_films(
                    params={
                        "with_origin_country": country.alpha_2,
                        "primary_release_year": year,
                    },
                )

    def get_film_detail(self, tmdb_id: int):
        return self.request("GET", f"/movie/{tmdb_id}")
