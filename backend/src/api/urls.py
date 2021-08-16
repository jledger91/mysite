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
    path('google_client_id/',
         views.GoogleClientIdView.as_view(),
         name='google_client_id'),
    path('is_authenticated/',
         views.IsAuthenticatedView.as_view(),
         name='is_authenticated'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('token/', token_views.obtain_auth_token, name='token'),
]
