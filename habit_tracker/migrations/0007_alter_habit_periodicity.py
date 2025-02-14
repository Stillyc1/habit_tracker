# Generated by Django 5.1.4 on 2025-01-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit_tracker", "0006_alter_habit_periodicity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.PositiveIntegerField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)],
                default=1,
                help_text="Выберите период привычки в днях.",
                verbose_name="Периодичность привычки. в днях",
            ),
        ),
    ]
