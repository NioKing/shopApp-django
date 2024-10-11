from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User

@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.email}")