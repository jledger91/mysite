from django.contrib.auth.models import User

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
        exclude=True,
    )
    average_score = filters.NumberFilter(
        'average_score',
        label='Average score',
        lookup_expr='exact',
    )
    average_score_floor = filters.NumberFilter(
        'average_score',
        label='Average score starts with',
        lookup_expr='startswith',
    )
    max_average_score = filters.NumberFilter(
        'average_score',
        label='Average score is less than or equal to',
        lookup_expr='lte',
    )
    min_average_score = filters.NumberFilter(
        'average_score',
        label='Average score is greater than or equal to',
        lookup_expr='gte',
    )
    reviewed_by = filters.ModelChoiceFilter(
        'review__user',
        label='Reviewed by',
        queryset=User.objects.all(),
    )
    ordering = filters.OrderingFilter(fields=[
        ('title', 'title_asc'),
        ('-title', 'title_desc'),
        ('release_date', 'release_date_asc'),
        ('-release_date', 'release_date_desc'),
        ('duration', 'duration_asc'),
        ('-duration', 'duration_desc'),
        # TODO: This currently just orders by character. Ideally, it
        #  wants to order like so: (U, PG, 12A, 12, 15, 18,)
        ('rating', 'rating_asc'),
        ('-rating', 'rating_desc'),
        ('average_score', 'average_score_asc'),
        ('-average_score', 'average_score_desc'),
    ])
