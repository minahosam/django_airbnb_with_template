# Generated by Django 3.1.3 on 2020-12-28 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_auto_20201227_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomreview',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_author', to='auth.user'),
            preserve_default=False,
        ),
    ]
