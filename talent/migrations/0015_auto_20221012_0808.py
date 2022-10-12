# Generated by Django 3.2.3 on 2022-10-12 01:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0014_interview_no_interview'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewnote',
            name='date_input',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewnote',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
