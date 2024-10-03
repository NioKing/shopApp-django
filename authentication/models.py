from django.db import models
import uuid
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    
    class UserRoles(models.TextChoices):
        CUSTOMER = "CUSTOMER", _("Customer")
        SELLER = "SELLER", _("Seller")
        ADMIN = "ADMIN", _("Admin")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=40, validators=[MinLengthValidator(6)])
    hashed_rt = models.CharField(null=True, max_length=255)
    role = models.CharField(max_length=20, choices=UserRoles, default=UserRoles.CUSTOMER)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
    
