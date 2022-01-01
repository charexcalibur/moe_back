from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from moerank.common.custom import CommonPagination, IsListOrIsAuthenticated, IsCreateOrIsAuthenticated
from rest_framework import serializers, viewsets
import requests
from moerank.dota.models import Matchlist, Matchdata
from moerank.dota.serializer.heros import MatchlistSerializer, MatchdataSerializer
from django.core.cache import caches

class GetMatchInfoViewSet(viewsets.ViewSet):
    throttle_classes = [AnonRateThrottle]
    permission_classes = (IsListOrIsAuthenticated,)

    def list(self, request):
        
        match_id = request.GET.get('matchId', None)
        print('matchId: ', match_id)
        try:
            if match_id:
                queryset = Matchlist.objects.using('matchinfo').filter(match_id=match_id).first()
                current_time = caches['realtime'].get(match_id)
                print('current_time: ', current_time)
                serializer = MatchlistSerializer(queryset)
                serializer.data['gametime'] = current_time
                print('serializer.data: ', serializer.data)
                return  Response(serializer.data)


            queryset = Matchlist.objects.using('matchinfo').all()

            if not queryset:
                return Response([])
            else:
                serializer = MatchlistSerializer(queryset, many=True)
                return Response(serializer.data)
        except Exception as e:
            print('GetMatchInfoViewSet error: ', e)
            return Response('', status=500)

class GetOldMatchScoreViewSet(viewsets.ViewSet):
    throttle_classes = [AnonRateThrottle]
    permission_classes = (IsListOrIsAuthenticated,)

    def list(self, request):
        match_id = request.GET.get('matchId', None)
        gametime = request.GET.get('gametime', None)


        queryset = Matchdata.objects.using('matchinfo').filter(match_id=match_id, gametime__lt=gametime).order_by('gametime')

        serializer = MatchdataSerializer(queryset, many=True)

        return Response(serializer.data)