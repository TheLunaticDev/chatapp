from django.urls import path
from . import views
from ads.views import show_ads_view, profile_view, delete_user_view

urlpatterns = [
    path("", show_ads_view, name="home"),
    path("profile/<str:username>/<int:page_no>/", profile_view, name="profile"),
    path("profile/delete/", delete_user_view, name="delete_user"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("terms_of_use/", views.terms_of_use, name="terms_of_use"),
    path("privacy_policy", views.privacy_policy, name="privacy_policy"),
]
