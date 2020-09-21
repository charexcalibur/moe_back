from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.cache import cache
import requests

class GetBlogAnalysisViewSet(ModelViewSet):

    def list(self, request):
        # cache.set('123', '321', timeout=7200)
        # cache_query = cache.get('123')
        try:
            r = requests.get('https://www.axis-studio.org/content.json')
            request_res = r.json()
        except:
            request_res = []
        print('res: ', request_res)
        res = {
            'error_no': '60001',
            'msg': 'ok',
            'result': ''
        }
        return Response(res)