# Generated by Django 4.0.5 on 2022-07-04 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_title', models.CharField(default='--problemTitle--', max_length=100)),
                ('problem_statement', models.TextField()),
                ('test_cases', models.FileField(null='True', upload_to='')),
                ('expected_output', models.FileField(null='True', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('submitted_code', models.FileField(upload_to='')),
                ('verdict', models.CharField(default='Running...', max_length=10)),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojApp.problems')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
