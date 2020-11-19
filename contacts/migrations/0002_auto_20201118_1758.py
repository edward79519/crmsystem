# Generated by Django 3.1.3 on 2020-11-18 09:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='start_time',
            field=models.DateField(default=datetime.datetime(2020, 11, 18, 9, 58, 42, 650569, tzinfo=utc)),
        ),
    ]
