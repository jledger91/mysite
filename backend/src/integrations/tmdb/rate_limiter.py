import backoff
from ratelimit import limits, sleep_and_retry
from requests.exceptions import HTTPError, RequestException

CALLS = 45
PERIOD_IN_SECONDS = 1


@sleep_and_retry
@limits(calls=CALLS, period=PERIOD_IN_SECONDS)
def rate_limited():
    return


def tmdb_rate_limit(func):
    @backoff.on_exception(
        backoff.expo,
        (HTTPError, RequestException),
        max_tries=5,
        jitter=backoff.full_jitter,
        giveup=lambda e: (
            isinstance(e, HTTPError)
            and e.response is not None
            and e.response.status_code not in [429, 500, 502, 503, 504]
        ),
    )
    def wrapper(*args, **kwargs):
        rate_limited()
        return func(*args, **kwargs)

    return wrapper
