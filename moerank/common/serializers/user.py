'''
@Description: Description
@Author: hayato
@Date: 2020-07-19 22:08:04
@LastEditors: hayato
@LastEditTime: 2020-07-20 17:00:37
'''
from rest_framework import serializers
from ..models import UserProfile, SocialMedia, CoserNoPic, CoserInfo, CoserSocialMedia

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

class CoserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoserInfo
        fields = "__all__"

class CoserNoPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoserNoPic
        fields = "__all__"

class CoserSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoserSocialMedia
        fields = "__all__"