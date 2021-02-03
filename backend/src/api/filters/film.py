from django_filters import rest_framework as filters

from mysite.models import Film


class FilmFilter(filters.FilterSet):
    """FilterSet for the Film API endpoint."""

    title = filters.CharFilter('title', lookup_expr='icontains')
    release_date = filters.DateFilter('release_date', lookup_expr='contains')
    released_before = filters.DateFilter('release_date', lookup_expr='lte')
    released_after = filters.DateFilter('release_date', lookup_expr='gte')
    duration = filters.DurationFilter('duration')
    min_duration = filters.DurationFilter('duration', lookup_expr='gte')
    max_duration = filters.DurationFilter('duration', lookup_expr='lte')
    synopsis = filters.CharFilter('synopsis', lookup_expr='icontains')
    rating = filters.MultipleChoiceFilter(
        'rating',
        choices=Film.RATING_CHOICES,
        lookup_expr='exact',
    )
    exclude_rating = filters.MultipleChoiceFilter(
        'rating',
        choices=Film.RATING_CHOICES,
        lookup_expr='exact',
        exclude=True
    )

    ordering = filters.OrderingFilter(fields=[
        ('title', 'title'),
        ('release_date', 'release_date'),
        ('duration', 'duration'),
        # TODO: This currently just orders by character. Ideally, it
        #  wants to order like so: (U, PG, 12A, 12, 15, 18,)
        ('rating', 'rating'),
    ])
