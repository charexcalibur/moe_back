# Generated by Django 3.0.8 on 2022-01-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0008_auto_20220104_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallpaper',
            name='lens',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='镜头'),
        ),
    ]