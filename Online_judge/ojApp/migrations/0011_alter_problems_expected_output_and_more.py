# Generated by Django 4.0.5 on 2022-07-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojApp', '0010_alter_problems_expected_output_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='expected_output',
            field=models.FileField(null='True', upload_to='oj_expected_outputs/'),
        ),
        migrations.AlterField(
            model_name='problems',
            name='test_cases',
            field=models.FileField(null='True', upload_to='oj_test_cases/'),
        ),
    ]