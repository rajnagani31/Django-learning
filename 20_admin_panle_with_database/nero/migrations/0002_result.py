# Generated by Django 5.2 on 2025-04-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nero", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Result",
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
                ("roll", models.IntegerField()),
                ("name", models.CharField(max_length=50)),
                ("CGPA", models.IntegerField()),
            ],
        ),
    ]
