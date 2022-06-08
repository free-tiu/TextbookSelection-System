# Generated by Django 3.2.4 on 2022-04-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclass', '0002_alter_tbook_b_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tclass',
        ),
        migrations.AlterModelOptions(
            name='tbook',
            options={'ordering': ['id'], 'verbose_name': '教材管理', 'verbose_name_plural': '教材管理'},
        ),
        migrations.AlterModelOptions(
            name='tpress',
            options={'verbose_name': '出版社管理', 'verbose_name_plural': '出版社管理'},
        ),
        migrations.AddField(
            model_name='tbook',
            name='price',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='价格'),
        ),
    ]