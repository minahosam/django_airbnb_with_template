# Generated by Django 3.1.3 on 2021-01-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20201229_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('image', models.ImageField(upload_to='places/')),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='location',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]