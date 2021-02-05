from django.urls import path, include

from rest_framework.authtoken import views as token_views
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()
router.register(r'films', views.FilmViewSet, basename='film')
router.register(r'reviews', views.ReviewViewSet, basename='review')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', token_views.obtain_auth_token),
]
