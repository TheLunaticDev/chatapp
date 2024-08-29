from django.urls import path
from .views import chat_list_view, conversation_view, start_conversation_view

urlpatterns = [
    path("", chat_list_view, name="chat_list"),
    path("<int:conversation_id>/", conversation_view, name="conversation_view"),
    path("new/<int:user_id>/", start_conversation_view, name="start_conversation_view"),
]
