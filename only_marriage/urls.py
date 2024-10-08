from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("ads/", include("ads.urls")),
    path("chat/", include("chat.urls")),
]
