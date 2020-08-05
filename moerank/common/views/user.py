'''
@Description: Description
@Author: hayato
@Date: 2020-07-19 22:06:51
@LastEditors: hayato
@LastEditTime: 2020-07-20 17:00:04
'''
from ..models import UserProfile, SocialMedia, CoserNoPic, CoserInfo, CoserSocialMedia
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..serializers.user import UserProfileSerializer, SocialMediaSerializer, CoserNoPicSerializer, CoserInfoSerializer, CoserSocialMediaSerializer

class UserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class SocialMediaViewSet(ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class CoserNoPicViewSet(ModelViewSet):
    queryset = CoserNoPic.objects.all()
    serializer_class = CoserNoPicSerializer

class CoserInfoSViewSet(ModelViewSet):
    queryset = CoserInfo.objects.all()
    serializer_class = CoserInfoSerializer

class CoserSocialMediaSViewSet(ModelViewSet):
    queryset = CoserSocialMedia.objects.all()
    serializer_class = CoserSocialMediaSerializer