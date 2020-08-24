from django.urls import path

from . import views

urlpatterns = [
    path("my-account", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]