from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_ads_view, name="create_ad"),
    path("info/<int:id>", views.ads_info_view, name="ad_info"),
    path("edit/<int:ad_id>", views.edit_ads_view, name="edit_ad"),
    path("flag/<int:ad_id>", views.flag_ad_view, name="flag_ad"),
    path("delete/<int:ad_id>/", views.delete_ad, name="delete_ad"),
    path("payment_success/<int:ad_id>/", views.payment_success, name="payment_success"),
    path(
        "payment_notification/",
        views.payment_notification_view,
        name="payment_notification",
    ),
]
