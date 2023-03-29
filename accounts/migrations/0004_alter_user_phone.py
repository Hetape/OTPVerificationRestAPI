# Generated by Django 4.0.4 on 2023-03-28 11:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Up to 13 digits allowed.', regex='^\\+?1?\\d{9,13}$')]),
        ),
    ]
