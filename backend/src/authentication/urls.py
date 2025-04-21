from authentication import views
from django.urls import path
from rest_framework.authtoken import views as token_views

app_name = "authentication"

urlpatterns = [
    path(
        "is_authenticated/",
        views.IsAuthenticatedView.as_view(),
        name="is_authenticated",
    ),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("token/", token_views.obtain_auth_token, name="token"),
]
