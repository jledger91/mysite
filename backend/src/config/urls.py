from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("config.api_v1_urls", namespace="api")),
    path("auth/", include("authentication.urls", namespace="auth")),
    path("oauth/", include("social_django.urls", namespace="social")),
]
