# Generated by Django 3.0.8 on 2021-03-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallpaper',
            name='full_hd_url',
        ),
        migrations.RemoveField(
            model_name='wallpaper',
            name='ultra_hd_url',
        ),
        migrations.AddField(
            model_name='wallpaper',
            name='des',
            field=models.CharField(default='', max_length=50, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='wallpaper',
            name='raw_url',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='raw 地址'),
        ),
        migrations.AddField(
            model_name='wallpaper',
            name='thumbnail_url',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='缩略图地址'),
        ),
        migrations.AddField(
            model_name='wallpaper',
            name='wallpaper_url',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='壁纸地址'),
        ),
    ]
