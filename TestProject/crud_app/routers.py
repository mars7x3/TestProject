from django.urls import re_path, path

from crud_app.consumers import NotificationConsumer


websocket_urlpatterns = [
    path(r"ws/notification/", NotificationConsumer.as_asgi()),
]
