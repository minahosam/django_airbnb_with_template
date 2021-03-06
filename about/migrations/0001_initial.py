# Generated by Django 3.1.3 on 2020-12-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_we_do', models.TextField(max_length=1000)),
                ('goal', models.TextField(max_length=1000)),
                ('mission', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'abouts',
            },
        ),
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=100000)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
