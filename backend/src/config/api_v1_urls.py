from config.views import ConfigView
from django.urls import include, path

app_name = "api_v1"

urlpatterns = [
    path("config", ConfigView.as_view(), name="config"),
    path("films", include("films.urls", namespace="films")),
    path("reviews", include("reviews.urls", namespace="reviews")),
    path("users", include("users.urls", namespace="users")),
]
