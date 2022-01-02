from rest_framework.viewsets import ModelViewSet
from ..models import WallPaper, ImageTag
from rest_framework.response import Response
from ..serializers.wallpaper import WallpaperSerializer, TagsSerializer
from moerank.common.custom import CommonPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from moerank.common.custom import IsListOrIsAuthenticated

class WallpaperViewSet(ModelViewSet):
    queryset = WallPaper.objects.all()
    serializer_class = WallpaperSerializer
    pagination_class = CommonPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uid']
    permission_classes = (IsListOrIsAuthenticated,)
    
    
class TagsViewSet(ModelViewSet):
    queryset = ImageTag.objects.all()
    serializer_class = TagsSerializer
    pagination_class = CommonPagination