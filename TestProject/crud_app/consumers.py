import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings


class NotificationConsumer(AsyncWebsocketConsumer):
    room = settings.WS_ROOM_NAME

    async def connect(self):
        await self.channel_layer.group_add(self.room, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        if self.room:
            await self.channel_layer.group_discard(self.room, self.channel_name)

    async def send_notification(self, event):
        await self.send(text_data=json.dumps(event))
