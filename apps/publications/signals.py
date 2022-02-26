from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Publication


@receiver(post_save, sender=Publication)
def publication_handler(sender, instance, created, **kwargs):
    if created:
        print(f'NEW СОЗДАЛАСЬ ПУБЛИКАЦИЯ')
    else:
        print('ПУБЛИКАЦИЯ ОБНОВИЛАСЬ')

