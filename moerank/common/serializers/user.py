'''
@Description: Description
@Author: hayato
@Date: 2020-07-19 22:08:04
@LastEditors: hayato
@LastEditTime: 2020-07-20 17:00:37
'''
from rest_framework import serializers
from ..models import UserProfile, SocialMedia, CoserNoPic, CoserInfo, CoserSocialMedia
import re

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']

class UserListSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    def get_roles(self, obj):
        return obj.roles.values()

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'mobile', 'email',
                  'is_active','roles']
        depth = 1

class UserModifySerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(max_length=11)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'mobile', 'email',
                  'is_active', 'roles']

    def validate_mobile(self, mobile):
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码不合法")
        return mobile

class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False)
    mobile = serializers.CharField(max_length=11)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'mobile', 'email', 'is_active', 'roles',
                  'password']

    def validate_username(self, username):
        if UserProfile.objects.filter(username=username):
            raise serializers.ValidationError(username + ' 账号已存在')
        return username

    def validate_mobile(self, mobile):
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码不合法")
        if UserProfile.objects.filter(mobile=mobile):
            raise serializers.ValidationError("手机号已经被注册")
        return mobile

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