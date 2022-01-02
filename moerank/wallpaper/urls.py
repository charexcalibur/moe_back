from django.urls import path, include
from moerank.wallpaper.views.wallpaper import WallpaperViewSet, TagsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'wallpapers', WallpaperViewSet, basename='wallpapers')
router.register(r'tags', TagsViewSet, basename='tags')

urlpatterns = [
    path(r'', include(router.urls))
]