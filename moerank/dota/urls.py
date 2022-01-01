from django.urls import path, include
from moerank.dota.views.heros import HerosViewSet, GetWinRateViewSet, HeroCacheControl
from moerank.dota.views.models import RankModelViewSet
from rest_framework import routers
from moerank.dota.views.realtime import AsyncConsumer
from moerank.dota.views.match import GetMatchInfoViewSet, GetOldMatchScoreViewSet

router = routers.DefaultRouter()
router.register(r'heros', HerosViewSet, basename='Heros')
router.register(r'rankmodels', RankModelViewSet, basename='rankmodels')

urlpatterns = [
    path(r'', include(router.urls)),
    path('getRate', GetWinRateViewSet.as_view({'post': 'create'})),
    path('cacheControl', HeroCacheControl.as_view({'get': 'list'})),
    path('getMatch', GetMatchInfoViewSet.as_view({'get': 'list'})),
    path('getOldMatchRate', GetOldMatchScoreViewSet.as_view({'get': 'list'}))
]