from django.urls import include, path
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet

app_name = "reviews"

router = DefaultRouter()
router.register(r"", ReviewViewSet, basename="reviews")

urlpatterns = [
    path("", include(router.urls)),
]
