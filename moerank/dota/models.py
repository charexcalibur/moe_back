from django.db import models

class TimeAbstract(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='添加时间')
    modify_time = models.DateTimeField(auto_now=True, blank=True, verbose_name='更新时间')

    class Meta:
        abstract = True

# Create your models here.
class Heros(models.Model):
    hero_type_choices = (
        ('1', '力量'),
        ('2', '敏捷'),
        ('3', '智力')
    )
    attack_type = (
        ('1', '近战'),
        ('2', '远程')
    )
    hero_id = models.IntegerField(blank=True, null=True, verbose_name='英雄id')
    hero_name = models.CharField(max_length=100, default='', verbose_name='英雄名称')
    localized_name = models.CharField(max_length=100, default='', verbose_name='本地英雄名称')
    avatar_url = models.URLField(max_length=200, default='', blank=True, null=True, verbose_name='头像地址')
    position_type = models.CharField(max_length=30, choices=hero_type_choices, default='', blank=True, verbose_name="英雄类型")

class RankModel(TimeAbstract):
    title = models.CharField(max_length=100, default='', verbose_name='模型标题')
    sub_title = models.CharField(max_length=100, default='', verbose_name='模型副标题')
    des = models.CharField(max_length=100, default='', blank=True, null=True, verbose_name='模型描述')
    rank_url = models.URLField(max_length=200, default='', blank=True, null=True, verbose_name='模型请求地址')
    is_show = models.BooleanField(default=True, verbose_name='是否展示')