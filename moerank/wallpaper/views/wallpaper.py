from rest_framework.viewsets import ModelViewSet
from ..models import WallPaper, ImageTag, ImageSize, ImageCategory, Equipment
from rest_framework.response import Response
from ..serializers.wallpaper import WallpaperSerializer, TagsSerializer, ImageSizeSerializer, ImageCategorySerializer, WallpaperListSerializer, EquipmentSerializer
from moerank.common.custom import CommonPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from moerank.common.custom import IsListOrIsAuthenticated

class WallpaperViewSet(ModelViewSet):
    queryset = WallPaper.objects.all()
    pagination_class = CommonPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'uid': ['exact'],
        'rate': ['exact', 'gte', 'range'],
        'tags': ['exact'],
        'categories': ['exact']
    }
    ordering_fields = ['add_time', 'rate']
    permission_classes = (IsListOrIsAuthenticated,)
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return WallpaperListSerializer
        else:
            return WallpaperSerializer
    
    
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
    
class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    pagination_class = CommonPagination