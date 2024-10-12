# Generated by Django 5.1.1 on 2024-10-10 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_user_id_cart_user'),
        ('product', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='carts', to='product.product'),
        ),
    ]