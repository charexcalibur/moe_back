from email.policy import default
from pyexpat import model
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
    tags = models.ManyToManyField('ImageTag', verbose_name=("标签"))
    rate = models.IntegerField(db_index=True, default=0, blank=True, null=True, verbose_name='评级')
    equipments = models.ManyToManyField('Equipment', verbose_name=('设备'))
    categories = models.ManyToManyField('ImageCategory', verbose_name=("类别"))
    is_shown = models.CharField(max_length=1, default=1, verbose_name='是否展示')
    shooting_date = models.CharField(db_index=True, max_length=50, default='', verbose_name='拍摄日期')
    
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
    type_choice = (
        (1, 'origin'),
        (2, '4k'),
        (3, 'thumbnail')
    )
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ForeignKey('WallPaper', null=True, on_delete=models.SET_NULL, verbose_name='image')
    width = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name='宽')
    height = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name='高')
    cdn_url = models.URLField(null=True, default='', blank=True, verbose_name='资源地址')
    type = models.CharField(max_length=50, choices=type_choice, default=1, blank=True, verbose_name='图片类型')
    color_range = models.JSONField(default=dict, blank=True, null=True, verbose_name='主色值')
    
class Equipment(TimeAbstract):
    type_choice = (
        (1, 'camera'),
        (2, 'lens'),
        (3, 'phone'),
        (4, 'drone')
    )
    name = models.CharField(max_length=50, default='', blank=True, null=True, verbose_name='器材名称')
    brand = models.CharField(max_length=50, default='', blank=True, null=True, verbose_name='品牌名称')
    type = models.CharField(max_length=50, choices=type_choice, default=1, blank=True, verbose_name='器材类型')
    remark = models.CharField(max_length=100, default='', blank=True, null=True, verbose_name='备注')
    
    def __str__(self):
        return self.name    
    
    
class Comment(TimeAbstract):
    verify_status_choices = (
        (0, '未审核'),
        (1, '已审核')
    )
    name = models.CharField(max_length=50, default='', blank=True, null=True, verbose_name='评论人')
    e_mail_address = models.URLField(null=True, default=None, blank=True, verbose_name='邮箱地址')
    comment = models.TextField(default='', blank=True, null=True, verbose_name='评论')
    pid = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True, related_name='comment_parent')
    photo = models.ForeignKey('WallPaper', on_delete=models.SET_NULL, null=True, blank=True)
    verify_status = models.CharField(max_length=1, choices=verify_status_choices, default=0, verbose_name='审核状态')