from django.urls import path, include
from moerank.fhc.views.quotations import QuotationsViewSet, QuotationsStatisticViewSet, RandomQuotationsViewSet, VoteQuotationsViewSet, VoteCountViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'quotations', QuotationsViewSet, basename='Quotations')

urlpatterns = [
    path(r'', include(router.urls)),
    path('quotationsStatistic', QuotationsStatisticViewSet.as_view({'get': 'list'})),
    path('randomQuotation', RandomQuotationsViewSet.as_view({'get': 'list'})),
    path('voteQuo', VoteQuotationsViewSet.as_view({'post': 'create'})),
    path('voteCount/<pk>', VoteCountViewSet.as_view({'get': 'retrieve'})),
]