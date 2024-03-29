import os

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from crud_app.models import ProductImage, Product
from django.conf import settings


def create_product_images(product_id, images_list):
    create_list = [ProductImage(product=product_id, image=image) for image in images_list]
    ProductImage.objects.bulk_create(create_list)


def delete_product_images(product_id, image_ids):
    ProductImage.objects.filter(product_id=product_id, id__in=image_ids).delete()


def send_general_notification(text):
    channel_layer = get_channel_layer()
    event = {'type': 'send_notification', "text": text}
    async_to_sync(channel_layer.group_send)(settings.WS_ROOM_NAME, event)

