from django.urls import path, include
from moerank.dota.views.heros import HerosViewSet, GetWinRateViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'heros', HerosViewSet, basename='Heros')

urlpatterns = [
    path(r'', include(router.urls)),
    path('getRate', GetWinRateViewSet.as_view({'post': 'create'}))
]