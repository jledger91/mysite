from django.urls import include, path
from films.views import FilmsViewSet
from rest_framework.routers import DefaultRouter

app_name = "films"

router = DefaultRouter()
router.register(r"", FilmsViewSet, basename="films")

urlpatterns = [
    path("", include(router.urls)),
]
