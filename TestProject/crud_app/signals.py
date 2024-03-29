from django.db.models.signals import post_save
from django.dispatch import receiver

from crud_app.models import Product
from crud_app.utils import send_general_notification


@receiver(post_save, sender=Product)
def create_product(sender, instance, created, **kwargs):
    if created:
        text = f'Создан товар "{instance.title}"'
        send_general_notification(text)


