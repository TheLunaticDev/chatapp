# Generated by Django 5.1 on 2024-08-25 06:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ads",
            new_name="ad",
        ),
        migrations.RenameModel(
            old_name="tags",
            new_name="tag",
        ),
    ]
