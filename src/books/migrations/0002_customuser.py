# Generated by Django 4.2.7 on 2023-11-23 23:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "registration_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
