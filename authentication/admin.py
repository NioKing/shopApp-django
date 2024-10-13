from django.contrib import admin
from cart.admin import CartInline
from .models import User

class UserAdmin(admin.ModelAdmin):
    inlines = [CartInline]
    list_display = ['email', 'role']
    fields = ('email', 'role', 'is_active', 'is_staff')


admin.site.register(User, UserAdmin)

