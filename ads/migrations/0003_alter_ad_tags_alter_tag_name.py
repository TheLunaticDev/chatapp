# Generated by Django 5.1 on 2024-08-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_rename_ads_ad_rename_tags_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="tags",
            field=models.ManyToManyField(blank=True, to="ads.tag"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
