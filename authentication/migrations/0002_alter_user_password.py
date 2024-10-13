# Generated by Django 5.1.1 on 2024-10-13 00:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=140, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]