# Generated by Django 3.0.8 on 2020-09-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='角色')),
                ('desc', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('permissions', models.ManyToManyField(blank=True, to='common.Permission', verbose_name='权限')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
    ]