from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_ads_view),
    path("info/<int:id>", views.ads_info_view),
    path("edit/", views.edit_ads_view),
]
