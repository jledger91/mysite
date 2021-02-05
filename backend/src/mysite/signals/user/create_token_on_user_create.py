from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User, dispatch_uid='create_token_on_user_create')
def create_token_on_user_create(sender, instance, created, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)
