from rest_framework.viewsets import ModelViewSet
from ..models import WallPaper
from rest_framework.response import Response
from ..serializers.wallpaper import WallpaperSerializer
from moerank.common.custom import CommonPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class WallpaperViewSet(ModelViewSet):
    queryset = WallPaper.objects.all()
    serializer_class = WallpaperSerializer
    pagination_class = CommonPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uid']