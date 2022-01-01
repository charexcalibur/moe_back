from django.db.models import fields
from rest_framework import serializers
from moerank.dota.models import Heros
from moerank.dota.models import Matchlist, Matchdata
from django.core.cache import caches

class MatchlistSerializer(serializers.ModelSerializer):

    gametime = serializers.SerializerMethodField()

    class Meta:
        model = Matchlist
        fields = '__all__'

    def get_gametime(self, obj):
        current_time = caches['realtime'].get(obj.match_id)
        return current_time


class HerosSerializer(serializers.ModelSerializer):
    """
    英雄序列化
    """

    class Meta:
        model = Heros
        fields = '__all__'

class MatchdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matchdata
        fields = '__all__'