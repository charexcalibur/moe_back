'''
@Description: Description
@Author: hayato
@Date: 2020-07-19 22:21:47
@LastEditors: hayato
@LastEditTime: 2020-07-20 17:01:03
'''
from django.urls import path, include
from moerank.common.views.user import UserViewSet, SocialMediaViewSet, CoserNoPicViewSet, CoserInfoSViewSet, CoserSocialMediaSViewSet, login, CurrentUserViewSet
from moerank.common.views.analysis import GetBlogAnalysisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'socialMedia', SocialMediaViewSet)
router.register(r'coserNoPic', CoserNoPicViewSet)
router.register(r'coserinfo', CoserInfoSViewSet)
router.register(r'coserSocialMedia', CoserSocialMediaSViewSet)
router.register(r'currentUser', CurrentUserViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path('login', login),
    path('getBlogAnalysis', GetBlogAnalysisViewSet.as_view({'get': 'list'}))
]