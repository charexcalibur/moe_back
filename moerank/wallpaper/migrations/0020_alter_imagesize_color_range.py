# Generated by Django 3.2.13 on 2022-06-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0019_imagesize_color_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesize',
            name='color_range',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='主色值'),
        ),
    ]
