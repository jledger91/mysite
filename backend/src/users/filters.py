from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    """FilterSet for the User API endpoint."""

    username = filters.CharFilter("username", lookup_expr="exact")
    first_name = filters.CharFilter("first_name", lookup_expr="exact")
    last_name = filters.CharFilter("last_name", lookup_expr="exact")
    email = filters.CharFilter("email", lookup_expr="exact")
    is_staff = filters.BooleanFilter("is_staff")
    is_superuser = filters.BooleanFilter("is_superuser")
    ordering = filters.OrderingFilter(
        fields=[
            ("username", "username"),
            ("first_name", "first_name"),
            ("last_name", "last_name"),
            ("email", "email"),
            ("is_staff", "is_staff"),
            ("is_superuser", "is_superuser"),
        ]
    )
