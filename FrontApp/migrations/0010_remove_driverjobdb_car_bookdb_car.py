# Generated by Django 5.0.3 on 2024-04-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontApp', '0009_driverjobdb_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverjobdb',
            name='Car',
        ),
        migrations.AddField(
            model_name='bookdb',
            name='Car',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
