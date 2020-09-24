from rest_framework import serializers
from moerank.fhc.models import Quotations

class QuotationsSerializer(serializers.ModelSerializer):
    '''
    语录序列化
    '''

    class Meta:
        model = Quotations
        fields = '__all__'