from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(unique=True, max_length=125)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
