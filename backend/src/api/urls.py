from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import FilmViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'films', FilmViewSet, basename='film')

urlpatterns = [
    path('', include(router.urls))
]
