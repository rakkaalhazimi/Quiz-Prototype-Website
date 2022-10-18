# Generated by Django 4.1 on 2022-10-17 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0003_alter_user_password_hash_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=255, validators=[django.core.validators.EmailValidator()]
            ),
        ),
    ]
