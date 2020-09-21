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
from ..serializers.user import UserProfileSerializer, SocialMediaSerializer, CoserNoPicSerializer, CoserInfoSerializer, CoserSocialMediaSerializer, CurrentUserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import json
from rest_framework.response import Response

User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CurrentUserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = CurrentUserSerializer

    def list(self, request):
        current_user = CurrentUserSerializer(request.user)
        print('current_user: ', current_user)
        res = {
            'result': current_user.data
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
        ret = {
            'error_no': '1004',
            'msg': 'succeed',
            'token': str(token)
        }
        return JsonResponse(ret, status=200, safe=False)
    else:
        ret = {
            'error_no': '1005',
            'msg': 'username or password is invaild'
        }
        return JsonResponse(ret, status=200, safe=False)        