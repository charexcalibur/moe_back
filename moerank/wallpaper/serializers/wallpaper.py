from rest_framework import serializers
from ..models import WallPaper, ImageTag, ImageSize, ImageCategory

class WallpaperSerializer(serializers.ModelSerializer):
    image_sizes = serializers.SerializerMethodField()
    
    def get_image_sizes(self, obj):
        return [item for item in ImageSize.objects.filter(image=obj.id).select_related('image')]
    
    class Meta:
        model = WallPaper
        fields = [
            'uid',
            'name', 
            'des', 
            'location', 
            'iso', 
            'aperture', 
            'shutter', 
            'focal_length',
            'tags',
            'rate',
            'categories',
            'image_sizes',
            'add_time',
            'modify_time',
            'equipment',
            'lens'
        ]
        
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTag
        fields = '__all__'
        
class ImageSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSize
        fields = '__all__'
        

class ImageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCategory
        fields = '__all__'