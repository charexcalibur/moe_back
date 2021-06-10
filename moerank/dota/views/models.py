from rest_framework.viewsets import ModelViewSet
from moerank.common.custom import CommonPagination, IsListOrIsAuthenticated, IsCreateOrIsAuthenticated
from moerank.dota.models import RankModel
from moerank.dota.serializer.models import RankModelSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
import requests
import json
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache


class RankModelViewSet(ModelViewSet):
    pagination_class = CommonPagination
    queryset = RankModel.objects.all()
    serializer_class = RankModelSerializer
    filter_backends = [DjangoFilterBackend]
    # authentication_classes = []
    permission_classes = (IsListOrIsAuthenticated,)