from rest_framework.viewsets import ModelViewSet
from ..models import Menu
from rest_framework.response import Response
from ..serializers.menu import MenuSerializer
from moerank.common.custom import CommonPagination, TreeAPIView, RbacPermission
from rest_framework.filters import SearchFilter, OrderingFilter

class MenuViewSet(ModelViewSet, TreeAPIView):
    perms_map = ({'*': 'admin'}, {'*': 'menu_all'}, {'get': 'menu_list'}, {'post': 'menu_create'}, {'put': 'menu_edit'},
                 {'delete': 'menu_delete'})
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('sort',)
    permission_classes = (RbacPermission,)

class MenuTreeView(TreeAPIView):
    queryset = Menu.objects.all()