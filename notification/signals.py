from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from authentication.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to our shop!',
            'Thank you for registering!',
            'shop@app.com',
            [instance.email],
            fail_silently=False,
        )


@receiver(post_delete, sender=User)
def send_email_on_delete(sender, instance, **kwargs):
    send_mail(
        'User deleted',
        f'User {instance.email} was deleted',
        'shop@app.com',
        [instance.email],
        fail_silently=False,
    )