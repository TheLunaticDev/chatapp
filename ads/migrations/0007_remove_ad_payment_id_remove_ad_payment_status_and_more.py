# Generated by Django 5.1 on 2024-08-28 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0006_ad_payment_id_ad_payment_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ad",
            name="payment_id",
        ),
        migrations.RemoveField(
            model_name="ad",
            name="payment_status",
        ),
        migrations.AddField(
            model_name="ad",
            name="is_paid",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_status", models.CharField(default="pending", max_length=20)),
                ("invoice_id", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "ad_p",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="ads.ad"
                    ),
                ),
            ],
        ),
    ]
