# Generated by Django 3.2.4 on 2022-05-10 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_users_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '用户列表', 'verbose_name_plural': '用户列表'},
        ),
    ]