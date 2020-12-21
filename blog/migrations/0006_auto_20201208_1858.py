# Generated by Django 3.1.3 on 2020-12-08 16:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201208_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='', max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 8, 16, 58, 8, 334745, tzinfo=utc)),
        ),
    ]
