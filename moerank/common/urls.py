'''
@Description: Description
@Author: hayato
@Date: 2020-07-19 22:21:47
@LastEditors: hayato
@LastEditTime: 2020-07-20 17:01:03
'''
from django.urls import path, include
from moerank.common.views.user import UserViewSet, SocialMediaViewSet, CoserNoPicViewSet, CoserInfoSViewSet, CoserSocialMediaSViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'socialMedia', SocialMediaViewSet)
router.register(r'coserNoPic', CoserNoPicViewSet)
router.register(r'coserinfo', CoserInfoSViewSet)
router.register(r'coserSocialMedia', CoserSocialMediaSViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]