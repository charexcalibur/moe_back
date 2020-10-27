from rest_framework.viewsets import ModelViewSet
from ..models import Menu
from rest_framework.response import Response
from ..serializers.menu import MenuSerializer
from moerank.common.custom import CommonPagination, TreeAPIView, RbacPermission
from rest_framework.filters import SearchFilter, OrderingFilter
from moerank.common.filters.filters import MenuFilterBackend

class MenuViewSet(ModelViewSet, TreeAPIView):
    perms_map = ({'*': 'admin'}, {'*': 'menu_all'}, {'get': 'menu_list'}, {'post': 'menu_create'}, {'put': 'menu_edit'},
                 {'delete': 'menu_delete'})
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = CommonPagination
    filter_backends = (MenuFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('sort',)
    permission_classes = (RbacPermission,)

    def list(self, request):
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        tree_dict = {}
        tree_data = []
        try:
            for item in serializer.data:
                tree_dict[item['id']] = item
            for i in tree_dict:
                if tree_dict[i]['pid']:
                    pid = tree_dict[i]['pid']
                    parent = tree_dict[pid]
                    parent.setdefault('children', []).append(tree_dict[i])
                else:
                    tree_data.append(tree_dict[i])
            results = tree_data
        except KeyError:
            results = serializer.data
        res = {
            'error_no': '2001',
            'results': results
        }
        return Response(res, status=200)

class MenuTreeView(TreeAPIView):
    """
    no need for now
    """
    queryset = Menu.objects.all()
    filter_backends = (MenuFilterBackend, SearchFilter, OrderingFilter)

    def list(self, request):
        queryset = self.filter_queryset(self.queryset)
        res = {
            'error_no': '',
            'results': ''
        }
        return Response(res, status=200)
