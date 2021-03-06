from django.db import models
import uuid

# Create your models here.
class WallPaper(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, default='', unique=True, verbose_name='壁纸名')
    des = models.CharField(max_length=50, default='', verbose_name='描述')
    thumbnail_url = models.URLField(null=True, unique=True, blank=True, verbose_name='缩略图地址')
    wallpaper_url = models.URLField(null=True, unique=True, blank=True, verbose_name='壁纸地址')
    raw_url = models.URLField(null=True, unique=True, blank=True, verbose_name='raw 地址')
