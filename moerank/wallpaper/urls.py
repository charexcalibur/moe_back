from django.urls import path, include
from moerank.wallpaper.views.wallpaper import WallpaperViewSet, TagsViewSet, ImageCategoryViewSet, ImageSizeViewSet, EquipmentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'wallpapers', WallpaperViewSet, basename='wallpapers')
router.register(r'tags', TagsViewSet, basename='tags')
router.register(r'category', ImageCategoryViewSet, basename='分类')
router.register(r'imagesizes', ImageSizeViewSet, basename='资源列表')
router.register(r'equipments', EquipmentViewSet, basename='设备列表')

urlpatterns = [
    path(r'', include(router.urls))
]