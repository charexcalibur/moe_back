'''
@Description: Description
@Author: hayato
@Date: 2020-07-19 20:34:00
@LastEditors: hayato
@LastEditTime: 2020-07-19 22:57:13
'''
"""moerank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
router = routers.DefaultRouter()

urlpatterns = [
    path(r'admin', admin.site.urls),
    path(r'api/', include('moerank.common.urls')),
    path(r'fhc/', include('moerank.fhc.urls')),
    path(r'wallpaper/', include('moerank.wallpaper.urls')),
    path(r'dota/', include('moerank.dota.urls')),
    path(r'exam/', include('moerank.exam.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
