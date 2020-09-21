from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.cache import cache
import requests

class GetBlogAnalysisViewSet(ModelViewSet):

    def list(self, request):
        blog_analysis = cache.get('blog_analysis')
        if not blog_analysis:
            try:
                r = requests.get('https://www.axis-studio.org/content.json')
                request_res = r.json()
            except:
                request_res = []
            
            if not request_res:
                res = {
                    'error_no': '60001',
                    'msg': 'no result',
                    'result': request_res
                }
                return Response(res)


            cache.set('blog_analysis', request_res, 7200)

            res = {
                'error_no': '60002',
                'msg': 'succeed',
                'result': {
                    'total_blog_count': len(request_res)
                }
            }

            return Response(res)
        else:
            res = {
                'error_no': '60002',
                'msg': 'succeed',
                'result': {
                    'total_blog_count': len(blog_analysis)
                }
            }

            return Response(res)            