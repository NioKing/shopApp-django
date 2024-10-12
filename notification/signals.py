from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.email}")
        # send_mail(
        #     'Welcome to our shop!',
        #     'Thank you for registering!',
        #     'noreply@example.com',
        #     [instance.email],
        #     fail_silently=False,
        # )

