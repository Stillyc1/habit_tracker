# Generated by Django 5.1.4 on 2025-01-08 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habit_tracker", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="habit",
            options={"verbose_name": "Привычка", "verbose_name_plural": "Привычки"},
        ),
    ]
