# Generated by Django 3.1.3 on 2020-12-27 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201225_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 27, 19, 6, 38, 183666, tzinfo=utc)),
        ),
    ]
