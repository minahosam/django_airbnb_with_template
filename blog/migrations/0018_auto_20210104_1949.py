# Generated by Django 3.1.3 on 2021-01-04 17:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20201229_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 17, 49, 6, 635515, tzinfo=utc)),
        ),
    ]