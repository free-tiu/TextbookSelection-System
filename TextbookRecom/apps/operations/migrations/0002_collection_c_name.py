# Generated by Django 3.2.4 on 2022-02-16 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='c_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏用户'),
        ),
    ]
