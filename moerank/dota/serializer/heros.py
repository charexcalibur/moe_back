from rest_framework import serializers
from moerank.dota.models import Heros

class HerosSerializer(serializers.ModelSerializer):
    """
    英雄序列化
    """

    class Meta:
        model = Heros
        fields = '__all__'