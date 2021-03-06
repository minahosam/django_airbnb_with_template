# Generated by Django 3.1.3 on 2020-12-04 21:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'managed': True, 'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQs'},
        ),
        migrations.AlterField(
            model_name='about',
            name='goal',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='mission',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='what_we_do',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='faq',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=100000),
        ),
        migrations.AlterModelTable(
            name='faq',
            table='',
        ),
    ]
