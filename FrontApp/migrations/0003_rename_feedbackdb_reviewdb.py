# Generated by Django 5.0.3 on 2024-04-03 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrontApp', '0002_rename_message_feedbackdb_review_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeedbackDB',
            new_name='ReviewDB',
        ),
    ]