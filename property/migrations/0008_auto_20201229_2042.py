# Generated by Django 3.1.3 on 2020-12-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20201229_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomreview',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
