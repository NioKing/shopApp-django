from django.contrib import admin
from cart.admin import CartInline
from .models import User

class UserAdmin(admin.ModelAdmin):
    inlines = [CartInline]


admin.site.register(User, UserAdmin)

