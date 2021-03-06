from django.urls import path, include
from moerank.wallpaper.views.wallpaper import WallpaperViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'wallpapers', WallpaperViewSet, basename='wallpapers')

urlpatterns = [
    path(r'', include(router.urls))
]