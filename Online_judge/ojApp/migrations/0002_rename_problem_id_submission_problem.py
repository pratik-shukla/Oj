# Generated by Django 4.0.5 on 2022-07-05 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ojApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='problem_id',
            new_name='problem',
        ),
    ]