# Generated by Django 3.1.3 on 2020-12-14 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201213_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 15, 30, 2, 459344, tzinfo=utc)),
        ),
    ]