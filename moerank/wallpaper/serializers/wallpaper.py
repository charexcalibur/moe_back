from rest_framework import serializers
from ..models import WallPaper, ImageTag

class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = WallPaper
        fields = '__all__'
        
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTag
        fields = '__all__'