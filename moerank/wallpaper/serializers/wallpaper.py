from rest_framework import serializers
from ..models import WallPaper

class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = WallPaper
        fields = '__all__'