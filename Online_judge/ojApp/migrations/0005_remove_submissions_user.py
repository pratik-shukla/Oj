# Generated by Django 4.0.5 on 2022-07-07 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ojApp', '0004_rename_submission_submissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissions',
            name='user',
        ),
    ]
