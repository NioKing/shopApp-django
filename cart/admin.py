from django.contrib import admin

from .models import Cart

class CartInline(admin.StackedInline):
    model = Cart
    can_delete = False
    verbose_name_plural = 'Cart'

class CartModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'updated_at')
    # ordering = ['updated_at', 'id']

admin.site.register(Cart, CartModelAdmin)
