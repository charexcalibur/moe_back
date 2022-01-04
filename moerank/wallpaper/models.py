from django.db import models
import uuid
from moerank.common.models import TimeAbstract

# Create your models here.
class WallPaper(TimeAbstract):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, default='', unique=True, verbose_name='壁纸名')
    des = models.CharField(max_length=50, default='',  blank=True, null=True, verbose_name='描述')
    location = models.CharField(max_length=50, default='', blank=True, null=True, verbose_name='地点')
    iso = models.CharField(max_length=50, default='',  blank=True, null=True, verbose_name='iso')
    aperture = models.CharField(max_length=50, default='', blank=True, null=True, verbose_name='光圈')
    shutter = models.CharField(max_length=50, default='', blank=True, null=True, verbose_name='快门')
    focal_length = models.CharField(max_length=50, default='', verbose_name='焦距')
    thumbnail_url = models.URLField(null=True, default=None, blank=True, verbose_name='缩略图地址')
    wallpaper_url = models.URLField(null=True, default=None, blank=True, verbose_name='壁纸地址')
    raw_url = models.URLField(null=True, default=None, blank=True, verbose_name='raw 地址')
    tags = models.ManyToManyField("ImageTag", verbose_name=("标签"))
    rate = models.IntegerField( default=0, blank=True, null=True, verbose_name='评级')
    equipment = models.CharField(max_length=50, default='', blank=True, null=True, verbose_name='器材')
    lens = models.CharField(max_length=50, default='', blank=True, null=True, verbose_name='镜头')
    categories = models.ManyToManyField("ImageCategory", verbose_name=("类别"))
    
    def __str__(self):
        return self.name

class ImageTag(TimeAbstract):
    tag_name = models.CharField(max_length=50, default='', unique=True, blank=True, null=True, verbose_name='标签名')
    
    def __str__(self):
        return self.tag_name

class ImageCategory(TimeAbstract):
    category_name = models.CharField(max_length=50, default='', unique=True, blank=True, null=True, verbose_name='类别')
    
    def __str__(self):
        return self.category_name
    
class ImageSize(TimeAbstract):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ForeignKey('WallPaper', null=True, on_delete=models.SET_NULL, verbose_name='image')
    width = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name='宽')
    height = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name='高')
    cdn_url = models.URLField(null=True, default='', blank=True, verbose_name='资源地址')