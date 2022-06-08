# Generated by Django 3.2.4 on 2022-02-20 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(blank=True, max_length=200, null=True, upload_to='user/', verbose_name='教材图片')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='教材名称')),
                ('press', models.CharField(blank=True, max_length=11, null=True, verbose_name='出版社')),
                ('author', models.CharField(blank=True, max_length=200, null=True, verbose_name='作者')),
                ('b_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='关联学科分类id')),
                ('date', models.CharField(blank=True, max_length=200, null=True, verbose_name='出版时间')),
                ('b_href', models.CharField(blank=True, max_length=200, null=True, verbose_name='详情页链接')),
                ('comment',  models.IntegerField(verbose_name="教材评论数", null=True, blank=True)),
                ('praise', models.IntegerField(verbose_name="好评率", null=True, blank=True)),
            ],
            options={
                'verbose_name': '教材信息',
                'verbose_name_plural': '教材信息',
            },
        ),
        migrations.CreateModel(
            name='tclass',
            fields=[
                ('id', models.CharField(blank=True, max_length=200, primary_key=True, serialize=False, verbose_name='学科分类id')),
                ('c_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='学科名称')),
                ('c_src', models.CharField(blank=True, max_length=200, null=True, verbose_name='学科链接')),
            ],
            options={
                'verbose_name': '学科分类',
                'verbose_name_plural': '学科分类',
            },
        ),
        migrations.CreateModel(
            name='tpress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='出版社id')),
                ('p_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='出版社名称')),
                ('p_src', models.CharField(blank=True, max_length=200, null=True, verbose_name='出版社链接')),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
            },
        ),
    ]