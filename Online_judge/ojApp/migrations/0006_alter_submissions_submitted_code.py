# Generated by Django 4.0.5 on 2022-07-07 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojApp', '0005_remove_submissions_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='submitted_code',
            field=models.FileField(upload_to='oj_received/'),
        ),
    ]
