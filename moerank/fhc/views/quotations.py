from rest_framework.viewsets import ModelViewSet
from moerank.fhc.models import Quotations
from moerank.fhc.serializers.quotations import QuotationsSerializer
from moerank.common.custom import CommonPagination, TreeAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

class QuotationsViewSet(ModelViewSet):
    queryset = Quotations.objects.all()
    serializer_class = QuotationsSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('content','author',)
    ordering_fields = ('add_time',)