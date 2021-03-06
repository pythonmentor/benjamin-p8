from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout",),
    path("profile/", views.profile, name="profile"),
    path("create_account/", views.create_account, name="create_account"),
    path("favorites/", views.favorites_user, name="favorites"),
]
