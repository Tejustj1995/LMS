# Generated by Django 2.1.15 on 2020-03-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_remove_employee_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='defaultdays',
        ),
        migrations.AddField(
            model_name='leave',
            name='defaultdays_casual',
            field=models.PositiveIntegerField(blank=True, default=7, null=True, verbose_name='Leave days per year counter'),
        ),
        migrations.AddField(
            model_name='leave',
            name='defaultdays_planned',
            field=models.PositiveIntegerField(blank=True, default=7, null=True, verbose_name='Leave days per year counter'),
        ),
        migrations.AddField(
            model_name='leave',
            name='defaultdays_sick',
            field=models.PositiveIntegerField(blank=True, default=7, null=True, verbose_name='Leave days per year counter'),
        ),
    ]
