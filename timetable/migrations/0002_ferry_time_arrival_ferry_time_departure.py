# Generated by Django 4.0.5 on 2022-07-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ferry',
            name='time_arrival',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='ferry',
            name='time_departure',
            field=models.TimeField(null=True),
        ),
    ]
