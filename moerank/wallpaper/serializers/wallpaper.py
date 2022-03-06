from pyexpat import model
from rest_framework import serializers
from ..models import WallPaper, ImageTag, ImageSize, ImageCategory, Equipment

class WallpaperListSerializer(serializers.ModelSerializer):
    image_sizes = serializers.SerializerMethodField()
    equipments = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    def get_image_sizes(self, obj):
        return [ImageSizeSerializerForWallpaper(item).data for item in ImageSize.objects.filter(image=obj.id).select_related('image')]

    def get_equipments(self, obj):
        return [
            {
                'name': item.name,
                'brand': item.brand,
                'type': item.type,
                'id': item.id
            } for item in obj.equipments.all() if obj.equipments
        ]
        
    def get_tags(self, obj):
        return [
            {
                'name': item.tag_name,
                'id': item.id
            } for item in obj.tags.all() if obj.tags
        ]
        
    def get_categories(self, obj):
        return [
            {
                'category_name': item.category_name,
                'id': item.id
            } for item in obj.categories.all() if obj.categories
        ]

    class Meta:
        model = WallPaper
        fields = [
            'id',
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
            'equipments',
            'shooting_date'
        ]
        
class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = WallPaper
        fields = '__all__'
        
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTag
        fields = '__all__'
        
class ImageSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSize
        fields = '__all__'

class ImageSizeSerializerForWallpaper(serializers.ModelSerializer):
    class Meta:
        model = ImageSize
        fields = [
            'width',
            'height',
            'cdn_url',
            'type',
            'uid',
            'id'
        ]

class ImageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCategory
        fields = '__all__'
        
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'