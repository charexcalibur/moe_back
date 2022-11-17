from rest_framework.viewsets import ModelViewSet
from moerank.common.models import Role
from ..serializers.role import RoleListSerializer
from moerank.common.custom import CommonPagination, TreeAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from moerank.common.custom import csrf
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleListSerializer
    pagination_class = CommonPagination
    authentication_classes = (csrf, SessionAuthentication, BasicAuthentication,TokenAuthentication)