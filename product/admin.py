from django.contrib import admin

from .models import Product, Product_Image

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

class ProductImageInline(admin.StackedInline):
    model = Product_Image
    extra = 1

ProductAdmin.inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Image)