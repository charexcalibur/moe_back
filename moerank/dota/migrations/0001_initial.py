# Generated by Django 3.0.8 on 2021-06-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    # initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_id', models.IntegerField(blank=True, null=True, verbose_name='英雄id')),
                ('hero_name', models.CharField(default='', max_length=100, verbose_name='英雄名称')),
                ('localized_name', models.CharField(default='', max_length=100, verbose_name='本地英雄名称')),
                ('avatar_url', models.URLField(blank=True, default='', null=True, verbose_name='头像地址')),
                ('position_type', models.CharField(blank=True, choices=[('1', '力量'), ('2', '敏捷'), ('3', '智力')], default='', max_length=30, verbose_name='英雄类型')),
            ],
        ),
        migrations.CreateModel(
            name='RankModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(default='', max_length=100, verbose_name='模型标题')),
                ('sub_title', models.CharField(default='', max_length=100, verbose_name='模型副标题')),
                ('des', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='模型描述')),
                ('rank_url', models.URLField(blank=True, default='', null=True, verbose_name='模型请求地址')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
