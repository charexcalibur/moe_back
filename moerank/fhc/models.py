from django.db import models
import uuid

class TimeAbstract(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True

class Quotations(TimeAbstract):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(default='', blank=True, verbose_name='内容')
    author = models.CharField(max_length=100, default='', verbose_name='作者')
    image_url = models.URLField(max_length=200, default='', blank=True, null=True, verbose_name='图片地址')

class QuotationsVote(TimeAbstract):
    qv_id = models.UUIDField(default=uuid.uuid4, editable=False)
    quotation = models.ForeignKey('Quotations', null=True, on_delete=models.SET_NULL, verbose_name='语录')
    votes = models.IntegerField(blank=True, null=True, default=1, verbose_name='票数')