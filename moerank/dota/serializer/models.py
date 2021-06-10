from django.db.models import fields
from rest_framework import serializers
from moerank.dota.models import RankModel

class RankModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankModel
        fields = '__all__'