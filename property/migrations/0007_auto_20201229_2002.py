# Generated by Django 3.1.3 on 2020-12-29 18:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_roomreview_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomreview',
            name='feedback',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]