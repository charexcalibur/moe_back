from rest_framework.viewsets import ModelViewSet
from moerank.fhc.models import Quotations
from moerank.fhc.serializers.quotations import QuotationsSerializer
from moerank.common.custom import CommonPagination, TreeAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
import base64
from rest_framework.response import Response

class QuotationsViewSet(ModelViewSet):
    queryset = Quotations.objects.all()
    serializer_class = QuotationsSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('content','author',)
    ordering_fields = ('add_time',)

    def create(self, request):
        content = request.POST.get('content', None)
        if not content:
            res = {
                'error_no': '7001',
                'msg': 'content is required'
            }
            return Response(res)

        author = request.POST.get('author', None)
        if not author:
            res = {
                'error_no': '7002',
                'msg': 'author is required'
            }
            return Response(res)

        save_data = {
            'content': base64.b64encode(content.encode()),
            'author': base64.b64encode(author.encode())
        }

        p = Quotations.objects.create(**save_data)
        
        res = {
            'error_no': '7003',
            'result': QuotationsSerializer(p).data
        }
        return Response(res)

    def update(self, request, pk=None):
        content = request.POST.get('content', None)
        if not content:
            res = {
                'error_no': '7001',
                'msg': 'content is required'
            }
            return Response(res)

        author = request.POST.get('author', None)
        if not author:
            res = {
                'error_no': '7002',
                'msg': 'author is required'
            }
            return Response(res)

        save_data = {
            'content': base64.b64encode(content.encode()),
            'author': base64.b64encode(author.encode())
        }

        p = Quotations.objects.filter(id=pk).update(**save_data)

        res = {
            'error_no': '7004',
            'result': p
        }
        return Response(res)