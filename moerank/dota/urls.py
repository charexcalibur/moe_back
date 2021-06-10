from django.urls import path, include
from moerank.dota.views.heros import HerosViewSet, GetWinRateViewSet, HeroCacheControl
from moerank.dota.views.models import RankModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'heros', HerosViewSet, basename='Heros')
router.register(r'rankmodels', RankModelViewSet, basename='rankmodels')

urlpatterns = [
    path(r'', include(router.urls)),
    path('getRate', GetWinRateViewSet.as_view({'post': 'create'})),
    path('cacheControl', HeroCacheControl.as_view({'get': 'list'}))
]