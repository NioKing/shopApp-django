from django.db import models
from authentication.models import User
from django.utils.translation import gettext_lazy as _
from product.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart", editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, blank=True, related_name='carts')


    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return self.user.email
    