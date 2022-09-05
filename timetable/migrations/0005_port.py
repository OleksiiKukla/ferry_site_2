# Generated by Django 4.0.5 on 2022-07-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timetable", "0004_ferry_date_alter_ferry_time_arrival_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Port",
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
                ("name", models.CharField(max_length=30)),
                ("country", models.CharField(max_length=30)),
            ],
        ),
    ]
