# Generated by Django 3.0.8 on 2020-07-20 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_coserinfo_name_en'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coserinfo',
            options={'ordering': ['id'], 'verbose_name': '社交平台', 'verbose_name_plural': '社交平台'},
        ),
    ]
