# Generated by Django 3.0.8 on 2022-01-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0011_auto_20220115_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallpaper',
            name='equipments',
        ),
        migrations.AddField(
            model_name='wallpaper',
            name='equipments',
            field=models.ManyToManyField(to='wallpaper.Equipment', verbose_name='设备'),
        ),
    ]
