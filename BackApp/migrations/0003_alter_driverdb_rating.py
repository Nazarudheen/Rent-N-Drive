# Generated by Django 5.0.3 on 2024-03-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackApp', '0002_driverdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverdb',
            name='Rating',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
