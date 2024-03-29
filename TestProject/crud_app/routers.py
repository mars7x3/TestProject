from django.urls import path

from crud_app.consumers import NotificationConsumer


websocket_urlpatterns = [
    path(r"ws/notification/", NotificationConsumer.as_asgi()),
]
