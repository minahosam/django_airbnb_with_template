# Generated by Django 3.1.3 on 2020-12-24 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0002_room_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombook',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
