from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from films.models import Film


class ReviewFilter(filters.FilterSet):
    """FilterSet for the Review API endpoint."""

    user = filters.ModelChoiceFilter(queryset=User.objects.all())
    film = filters.ModelChoiceFilter(queryset=Film.objects.all())
    date_submitted = filters.DateFilter("date_submitted", lookup_expr="contains")
    submitted_before = filters.DateFilter("date_submitted", lookup_expr="lte")
    submitted_after = filters.DateFilter("date_submitted", lookup_expr="gte")
    review = filters.CharFilter("review", lookup_expr="icontains")
    rating = filters.NumberFilter("rating", lookup_expr="exact")
    ordering = filters.OrderingFilter(
        fields=[
            ("user", "user"),
            ("film", "film"),
            ("date_submitted", "date_submitted"),
            ("rating", "rating"),
        ]
    )
