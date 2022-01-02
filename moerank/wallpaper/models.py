from django.db import models
import uuid
from moerank.common.models import TimeAbstract

# Create your models here.
class WallPaper(TimeAbstract):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, default='', unique=True, verbose_name='壁纸名')
    des = models.CharField(max_length=50, default='', verbose_name='描述')
    thumbnail_url = models.URLField(null=True, default=None, blank=True, verbose_name='缩略图地址')
    wallpaper_url = models.URLField(null=True, default=None, blank=True, verbose_name='壁纸地址')
    raw_url = models.URLField(null=True, default=None, blank=True, verbose_name='raw 地址')
    tags = models.ManyToManyField("ImageTag", verbose_name=("标签"))

class ImageTag(TimeAbstract):
    tag_name = models.CharField(max_length=50, default='', unique=True, blank=True, null=True, verbose_name='标签名')
    
    def __str__(self):
        return self.tag_name