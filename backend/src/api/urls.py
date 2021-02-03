from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import FilmViewSet, ReviewViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'films', FilmViewSet, basename='film')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls))
]
