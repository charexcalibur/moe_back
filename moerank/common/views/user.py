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
from ..serializers.user import UserProfileSerializer, SocialMediaSerializer, CoserNoPicSerializer, CoserInfoSerializer, CoserSocialMediaSerializer, CurrentUserSerializer, UserCreateSerializer, UserModifySerializer, UserListSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework.response import Response
from ..code import *

User = get_user_model()

class UserInfoView(APIView):
    @classmethod
    def get_permission_from_role(self, request):
        try:
            if request.user:
                perms_list = []
                for item in request.user.roles.values('permissions__method').distinct():
                    perms_list.append(item['permissions__method'])
                return perms_list
        except AttributeError:
            return None
    def get_permission_from_id(self, id):
        perms_list = []
        for item in UserProfile.objects.filter(id=id).first().roles.values('permissions__method').distinct():
            perms_list.append(item['permissions__method'])
        return perms_list

    def get(self, request):
        try:
            query_id = request.GET['user']
            perms = self.get_permission_from_id(query_id)
            data = {
                'id': request.user.id,
                'username': request.user.username,
                'email': request.user.email,
                'is_active': request.user.is_active,
                'createTime':request.user.date_joined,
                'roles': perms
            }
            return Response(data, status=OK)
        except:
            if request.user.id is not None:
                perms = self.get_permission_from_role(request)
                data = {
                    'id': request.user.id,
                    'username': request.user.username,
                    'email': request.user.email,
                    'is_active': request.user.is_active,
                    'createTime':request.user.date_joined,
                    'roles': perms
                }
                return Response(data, status=OK)
            else:
                return Response('请登录后访问!', status=FORBIDDEN)

class UserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'list':
            return UserListSerializer
        return UserModifySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    def partial_update(self, request, pk=None):
        save_data = request.data
        instance = UserProfile.objects.filter(id=pk).first()
        serializer = self.get_serializer(instance, data=save_data, partial=True)
        serializer.is_valid()
        serializer.save()
        print('serializer.errors: ', serializer.errors)
        return Response(serializer.data, status=OK)

    @csrf_exempt
    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated],
            url_path='change-passwd', url_name='change-passwd')
    def set_password(self, request, pk=None):
        print('set_password_request: ', request)
        perms = UserInfoView.get_permission_from_role(request)
        user = UserProfile.objects.get(id=pk)
        print('set_password_user: ', user)
        if 'admin' in perms or 'user_all' in perms or request.user.is_superuser:
            new_password1 = request.data['new_password1']
            new_password2 = request.data['new_password2']
            if new_password1 == new_password2:
                user.set_password(new_password2)
                user.save()
                return Response('密码修改成功!')
            else:
                return Response('新密码两次输入不一致!', status=BAD)
        else:
            old_password = request.data['old_password']
            print('old_password: ', old_password)
            if check_password(old_password, user.password):
                new_password1 = request.data['new_password1']
                new_password2 = request.data['new_password2']
                if new_password1 == new_password2:
                    user.set_password(new_password2)
                    user.save()
                    return Response('密码修改成功!', status=OK)
                else:
                    return Response('新密码两次输入不一致!', status=BAD)
            else:
                return Response('旧密码错误!', status=BAD)            

class CurrentUserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = CurrentUserSerializer

    def list(self, request):
        current_user = CurrentUserSerializer(request.user)
        roles = [item.name for item in request.user.roles.all()]
        res = {
            'result': {
                'current_user': current_user.data['username'],
                'roles': roles
            }
        }
        return Response(res)

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

@csrf_exempt
def login(request):
    request_method = request.method
    print('request_method: ', request_method)
    if request_method != 'POST':
        ret = {
            'error_no': '1001',
            'msg': 'only POST method is allowed'
        }
        return JsonResponse(ret, status=200, safe=False)
    
    # user_name = request.POST.get('username', None)
    # print('request.POST: ', request.body.username)
    request_data = json.loads(request.body)
    print('request_data: ', request_data)
    user_name = request_data.get('username', None)
    if not user_name:
        ret = {
            'error_no': '1002',
            'msg': 'username is required'
        }
        return JsonResponse(ret, status=200, safe=False)

    pwd = request_data.get('password', None)
    print('pwd: ', pwd)
    if not pwd:
        ret = {
            'error_no': '1003',
            'msg': 'password is required'
        }
        return JsonResponse(ret, status=200, safe=False)

    user = authenticate(request, username=user_name, password=pwd)
    if user:
        django_login(request, user)
        token = Token.objects.get_or_create(user=user)[0]
        roles = [item.name for item in request.user.roles.all()]
        menus = [item['menus__path'] for item in request.user.roles.values('menus__path')]

        ret = {
            'error_no': '1004',
            'msg': 'succeed',
            'token': str(token),
            'currentAuthority': roles,
            'menu': menus
        }
        return JsonResponse(ret, status=200, safe=False)
    else:
        ret = {
            'error_no': '1005',
            'msg': 'username or password is invaild'
        }
        return JsonResponse(ret, status=200, safe=False)        