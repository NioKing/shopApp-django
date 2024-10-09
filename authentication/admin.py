from django.contrib import admin
from cart.admin import CartInline
from .models import User

class UserAdmin(admin.ModelAdmin):
    inlines = [CartInline]
    list_display = ['email', 'role']
    fields = ('email', 'password', 'role')


admin.site.register(User, UserAdmin)

