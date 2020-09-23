from django.db import models
import uuid

class TimeAbstract(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True

class Quotations(TimeAbstract):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(default='', blank=True, verbose_name='内容')
    author = models.CharField(max_length=100, default='', verbose_name='作者')
