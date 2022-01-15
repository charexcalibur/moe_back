from rest_framework import filters
from ..models import WallPaper

class WallPaperFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_authenticated:
            return queryset
        return queryset.filter(is_shown=1)