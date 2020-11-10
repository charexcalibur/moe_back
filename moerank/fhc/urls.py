from django.urls import path, include
from moerank.fhc.views.quotations import QuotationsViewSet, QuotationsStatisticViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'quotations', QuotationsViewSet, basename='Quotations')

urlpatterns = [
    path(r'', include(router.urls)),
    path('quotationsStatistic', QuotationsStatisticViewSet.as_view({'get': 'list'}))
]