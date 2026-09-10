from django.urls import path

from .views import feedback_view
from .chat import chat_view

urlpatterns = [
    path("api/feedback/", feedback_view, name="feedback"),
    path("api/chat/", chat_view, name="chat"),
]
