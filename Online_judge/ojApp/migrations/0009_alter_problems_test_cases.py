# Generated by Django 4.0.5 on 2022-07-07 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojApp', '0008_alter_problems_expected_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='test_cases',
            field=models.FileField(null='True', upload_to='oj_test_cases<built-in function id>/'),
        ),
    ]