from rest_framework.viewsets import ModelViewSet
from moerank.common.models import Role
from ..serializers.role import RoleListSerializer
from moerank.common.custom import CommonPagination, TreeAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleListSerializer
    pagination_class = CommonPagination