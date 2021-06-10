from rest_framework import filters
from ..models import Menu

class MenuFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        perms = request.user.roles.values(
            'permissions__method',
        ).distinct()

        perms_list = [item['permissions__method'] for item in perms]
        print('perms_list: ', perms_list)

        if 'admin' in perms_list:
            return queryset
        else:
            menus_id_list = [item['menus'] for item in request.user.roles.values('menus')]
            return queryset.filter(id__in=menus_id_list)