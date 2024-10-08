# Generated by Django 5.1 on 2024-09-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0010_alter_ad_category_alter_ad_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="category",
            field=models.CharField(
                choices=[
                    (None, ""),
                    ("sp", "Strictly Platonic ($5)"),
                    ("ww", "Women seeking Women ($5)"),
                    ("wm", "Women seeking Men (Free)"),
                    ("mw", "Men seeking Women ($5)"),
                    ("mm", "Men seeking Men ($5)"),
                    ("mr", "Misc Romance ($5)"),
                ],
                max_length=2,
            ),
        ),
    ]
