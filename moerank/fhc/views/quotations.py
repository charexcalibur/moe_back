from rest_framework.viewsets import ModelViewSet
from moerank.fhc.models import Quotations
from moerank.fhc.serializers.quotations import QuotationsSerializer, QuotationsListSerializer
from moerank.common.custom import CommonPagination, TreeAPIView, RbacPermission, IsListOrIsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
import base64
from rest_framework.response import Response
import json
from django.core.cache import cache
from moerank.common.views.notice import Notice
import base64
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from moerank.common.tasks import notice
import random
from rest_framework import viewsets

class QuotationsViewSet(ModelViewSet):
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    throttle_classes = [UserRateThrottle]
    search_fields = ('content','author',)
    ordering_fields = ('add_time',)
    perms_map = ({'*': 'admin'}, {'*': 'quotations_all'}, {'get': 'quotations_list'}, {'post': 'quotations_create'}, {'put': 'quotations_edit'},
                 {'delete': 'quotations_delete'})
    permission_classes = (RbacPermission,)

    def get_serializer_class(self):
        if self.action == 'create':
            return QuotationsSerializer
        elif self.action == 'list':
            return QuotationsListSerializer
        return QuotationsSerializer

    def get_queryset(self):
        queryset = cache.get('quotations_queryset')
        if not queryset:
            queryset = Quotations.objects.all()
            cache.set('quotations_queryset', queryset, 60*60*2)
        return queryset

    def create(self, request):
        request_body_unicode = request.body.decode()
        if not request_body_unicode:
            content = request.POST.get('content', '')
            # if not content:
            #     res = {
            #         'error_no': '7001',
            #         'msg': 'content is required'
            #     }
            #     return Response(res)

            author = request.POST.get('author', None)
            if not author:
                res = {
                    'error_no': '7002',
                    'msg': 'author is required'
                }
                return Response(res)

            image_url = request.POST.get('image_url', '')
        else:
            request_body = json.loads(request_body_unicode)
            content = request_body.get('content', '')
            # if not content:
            #     res = {
            #         'error_no': '7001',
            #         'msg': 'content is required'
            #     }
            #     return Response(res)            
            author = request_body.get('author', None)
            if not author:
                res = {
                    'error_no': '7002',
                    'msg': 'author is required'
                }
                return Response(res)            
            image_url = request_body.get('image_url', None)

        save_data = {
            'content': base64.b64encode(content.encode()),
            'author': base64.b64encode(author.encode()),
            'image_url': image_url
        }

        p = Quotations.objects.create(**save_data)
        cache.delete('quotations_queryset')
        
        res = {
            'error_no': '7003',
            'result': QuotationsSerializer(p).data
        }
        # Notice.notice({
        #     'text': '新增语录通知',
        #     'desp': '内容 {}, 作者 {}'.format(content, author)
        # })
        markdown_str = '![]({})'.format(image_url)
        notice.delay({
            'text': '新增语录通知',
            'desp': ' {} 这个 b 说 {}，还贴了一张图 {}'.format(author, content, markdown_str)            
        })
        return Response(res)

    def update(self, request, pk=None):
        request_body_unicode = request.body.decode()
        if not request_body_unicode:
            content = request.POST.get('content', '')
            # if not content:
            #     res = {
            #         'error_no': '7001',
            #         'msg': 'content is required'
            #     }
            #     return Response(res)

            author = request.POST.get('author', None)
            if not author:
                res = {
                    'error_no': '7002',
                    'msg': 'author is required'
                }
                return Response(res)

            image_url = request.POST.get('image_url', '')
              
        else:
            request_body = json.loads(request_body_unicode)
            content = request_body.get('content', '')
            # if not content:
            #     res = {
            #         'error_no': '7001',
            #         'msg': 'content is required'
            #     }
            #     return Response(res)            
            author = request_body.get('author', None)
            if not author:
                res = {
                    'error_no': '7002',
                    'msg': 'author is required'
                }
                return Response(res)
            
            image_url = request_body.get('image_url', '')

        save_data = {
            'content': base64.b64encode(content.encode()),
            'author': base64.b64encode(author.encode()),
            'image_url': image_url
        }
        Q_queryset = Quotations.objects.filter(id=pk).first()
        old_content = base64.b64decode(Q_queryset.content[2:-1]).decode('utf-8')
        old_author = base64.b64decode(Q_queryset.author[2:-1]).decode('utf-8')

        p = Quotations.objects.filter(id=pk).update(**save_data)
        cache.delete('quotations_queryset')

        old_pic_markdown = '![]({})'.format(Q_queryset.image_url)
        new_pic_markdown = '![]({})'.format(image_url)

        notice.delay({
            'text': '修改语录通知',
            'desp': '内容 {} 修改为 {}, 作者 {} 修改为 {}, 图片 {} 修改为 {}'.format(old_content, content, old_author, author, old_pic_markdown, new_pic_markdown)            
        })        

        res = {
            'error_no': '7004',
            'result': p
        }
        return Response(res)

class QuotationsStatisticViewSet(ModelViewSet):
    queryset = Quotations.objects.all()
    serializer_class = QuotationsListSerializer
    # perms_map = ({'*': 'admin'}, {'*': 'quotations_all'}, {'get': 'quotations_statistic_list'})
    # permission_classes = (RbacPermission,)

    def list(self, request):
        queryset = self.get_queryset()
        total_quotations = queryset.count()

        res = {
            'total_quotations': total_quotations
        }
        return Response(res)

class RandomQuotationsViewSet(viewsets.ViewSet):
    throttle_classes = [AnonRateThrottle]
    authentication_classes = []
    permission_classes = (IsListOrIsAuthenticated,)
    def list(self, request):
        queryset = Quotations.objects.all()
        random_item = random.sample(list(queryset), 1)[0]
        serializer = QuotationsListSerializer(random_item)
        return Response(serializer.data)