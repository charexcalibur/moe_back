from rest_framework.viewsets import ModelViewSet
from ..models import WallPaper, ImageTag, ImageSize, ImageCategory, Equipment, Comment
from rest_framework.response import Response
from ..serializers.wallpaper import WallpaperSerializer, TagsSerializer, ImageSizeSerializer, ImageCategorySerializer, WallpaperListSerializer, EquipmentSerializer, CommentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from moerank.common.custom import CommonPagination, IsListOrIsAuthenticated, IsCreateOrIsAuthenticated, VotePostThrottle
from ..filters.filters import WallPaperFilterBackend
from moerank.common.tasks import notice

class WallpaperViewSet(ModelViewSet):
    queryset = WallPaper.objects.all()
    pagination_class = CommonPagination
    filter_backends = [WallPaperFilterBackend, DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'uid': ['exact'],
        'rate': ['exact', 'gte', 'range'],
        'tags': ['exact'],
        'categories': ['exact']
    }
    ordering_fields = ['add_time', 'rate', 'shooting_date']
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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['uid', 'image__id']
    serializer_class = ImageSizeSerializer
    pagination_class = CommonPagination
    
class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    pagination_class = CommonPagination
    
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['verify_status', 'id', 'pid', 'photo__id']
    serializer_class = CommentSerializer
    pagination_class = CommonPagination
    permission_classes = (IsCreateOrIsAuthenticated,)
    throttle_classes = [VotePostThrottle]
    ordering_fields = ['add_time']
    
    
    def create(self, request, *args, **kwargs):
        comment = request.data.get('comment')
        name = request.data.get('name')
        notice.delay({
            'text': '评论审核通知',
            'desp': f'{name} 评论了 {comment}'
        })
        return super().create(request, *args, **kwargs)