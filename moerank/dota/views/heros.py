from rest_framework.viewsets import ModelViewSet
from moerank.common.custom import CommonPagination, IsListOrIsAuthenticated, IsCreateOrIsAuthenticated
from moerank.dota.models import Heros
from moerank.dota.serializer.heros import HerosSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
import requests
import json
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache

class HerosViewSet(ModelViewSet):
    pagination_class = CommonPagination
    queryset = Heros.objects.all()
    serializer_class = HerosSerializer
    throttle_classes = [AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['position_type']
    authentication_classes = []
    permission_classes = (IsListOrIsAuthenticated,)    
    
class GetWinRateViewSet(viewsets.ViewSet):
    throttle_classes = [AnonRateThrottle]
    permission_classes = (IsCreateOrIsAuthenticated,)

    def create(self, request):
        request_body_unicode = request.body.decode()
        request_body = json.loads(request_body_unicode)        
        hero_id_list = request_body.get('hero_list', None)

        print('hero_id_list: ', hero_id_list)
        if not hero_id_list:
            res = {
                'error_no': '10001',
                'msg': 'hero id list is required'
            }
            return Response(res)

        
        headers = {'Content-Type': 'application/json'}

        data = {
            'data': hero_id_list
        }

        with open('/home/moeback/moerank/common/key.json', 'r') as f:
            json_data = json.load(f)

        url = json_data['winrate_url']


        r = requests.post(url, data=json.dumps(data))
        
        res = {
            'msg': 'ok',
            'results': r.json()
        }
        return Response(res)


class HeroCacheControl(viewsets.ViewSet):
    permission_classes = (IsListOrIsAuthenticated,)

    def list(self, request):
        query_string = request.query_params
        if query_string:
            change = query_string['change']
            if change == 'true':
                res = {
                    'isCache': True
                }
                cache.set('is_cache', res)
                return Response(res)
            elif change == 'false':
                res = {
                    'isCache': False
                }
                cache.set('is_cache', res)
                return Response(res)
            else:
                res = {
                    'msg': 'true or false'
                }
                return Response(res)

        is_cache = cache.get('is_cache')
        if not is_cache:
            res = {
                'isCache': True
            }
            cache.set('is_cache', res)
            return Response(res)
        else:
            return Response(is_cache)