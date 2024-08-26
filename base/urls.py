from django.urls import path
from . import views
from ads.views import show_ads_view

urlpatterns = [
    path("", show_ads_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
