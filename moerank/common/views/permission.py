from rest_framework.viewsets import ModelViewSet
from ..models import Permission
from ..serializers.permission import PermissionListSerializer
from moerank.common.custom import CommonPagination, TreeAPIView, RbacPermission
from rest_framework.filters import SearchFilter, OrderingFilter

class PermissionViewSet(ModelViewSet, TreeAPIView):
    '''
    权限：增删改查
    '''
    perms_map = ({'*': 'admin'}, {'*': 'permission_all'}, {'get': 'permission_list'}, {'post': 'permission_create'},
                 {'put': 'permission_edit'},{'delete': 'permission_delete'})
    queryset = Permission.objects.all()
    serializer_class = PermissionListSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
    permission_classes = (RbacPermission,)