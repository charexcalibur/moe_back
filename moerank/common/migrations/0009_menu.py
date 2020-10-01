# Generated by Django 3.0.8 on 2020-09-28 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_userprofile_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='菜单名')),
                ('icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='图标')),
                ('path', models.CharField(blank=True, max_length=158, null=True, verbose_name='链接地址')),
                ('is_frame', models.BooleanField(default=False, verbose_name='外部菜单')),
                ('is_show', models.BooleanField(default=True, verbose_name='显示标记')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='排序标记')),
                ('component', models.CharField(blank=True, max_length=200, null=True, verbose_name='组件')),
                ('url', models.CharField(blank=True, max_length=158, null=True, verbose_name='外站地址')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Menu', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'ordering': ['id'],
            },
        ),
    ]