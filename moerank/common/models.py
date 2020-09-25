'''
@Description: Description
@Author: hayato
@Date: 2020-07-19 20:34:57
@LastEditors: hayato
@LastEditTime: 2020-07-20 17:56:50
'''
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, default='', unique=True, verbose_name='用户名')
    mobile = models.CharField(max_length=11, null=True, unique=True, blank=True,  default='', verbose_name='手机号码')
    email = models.EmailField(max_length=50, null=True, unique=True, blank=True,  verbose_name='邮箱')
    roles = models.ManyToManyField('Role', verbose_name='角色', blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

class CoserInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, default='', unique=True, verbose_name='用户名')
    name_en = models.CharField(max_length=20, default='', unique=True, verbose_name='英文名')

    class Meta:
        verbose_name = '社交平台'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = name = models.CharField(max_length=20, default='', unique=True, verbose_name='平台名')

    class Meta:
        verbose_name = '社交平台'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

class CoserSocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coser = models.ForeignKey('CoserInfo', null=True, on_delete=models.SET_NULL, verbose_name='coser')
    social_media = models.ForeignKey('SocialMedia', null=True, on_delete=models.SET_NULL, verbose_name='social_media')
    url = models.URLField(null=True, unique=True, blank=True, verbose_name='社交软件地址')
    class Meta:
        verbose_name = 'coser社交平台关系'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        new_name = self.coser.name + ' - ' + self.social_media.name
        return new_name

class CoserNoPic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coser = models.ForeignKey('CoserInfo', null=True, on_delete=models.SET_NULL, verbose_name='coser')
    url = models.URLField(null=True, unique=True, blank=True, verbose_name='资源地址')

    class Meta:
        verbose_name = 'Coser资源'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='权限名')
    method = models.CharField(max_length=50, null=True, blank=True, verbose_name='方法')
    pid = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='父权限')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ['id']

class Role(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='角色')
    permissions = models.ManyToManyField('Permission', blank=True, verbose_name='权限')
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name='描述')

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name