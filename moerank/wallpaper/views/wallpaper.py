from rest_framework.viewsets import ModelViewSet
from ..models import WallPaper, ImageTag, ImageSize, ImageCategory
from rest_framework.response import Response
from ..serializers.wallpaper import WallpaperSerializer, TagsSerializer, ImageSizeSerializer, ImageCategorySerializer
from moerank.common.custom import CommonPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from moerank.common.custom import IsListOrIsAuthenticated

class WallpaperViewSet(ModelViewSet):
    queryset = WallPaper.objects.all()
    serializer_class = WallpaperSerializer
    pagination_class = CommonPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'uid': ['exact'],
        'rate': ['exact', 'gte', 'range']
    }
    ordering_fields = ['add_time', 'rate']
    permission_classes = (IsListOrIsAuthenticated,)
    
    
class TagsViewSet(ModelViewSet):
    queryset = ImageTag.objects.all()
    serializer_class = TagsSerializer
    pagination_class = CommonPagination
    
class ImageCategoryViewSet(ModelViewSet):
    queryset = ImageCategory.objects.all()
    serializer_class = ImageCategorySerializer
    pagination_class = CommonPagination
    
class ImageSizeViewSet(ModelViewSet):
    queryset = ImageSize.objects.all()
    serializer_class = ImageSizeSerializer
    pagination_class = CommonPagination