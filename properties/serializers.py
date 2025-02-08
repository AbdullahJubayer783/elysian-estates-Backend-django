from rest_framework import serializers
from .models import Property, PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, required=False)

    class Meta:
        model = Property
        fields = [
            'id',
            'estate_title',
            'segment_name',
            'description',
            'price',
            'status',
            'area',
            'location',
            'latitude',
            'longitude',
            'facilities',
            'images',
            'created_at',
            'updated_at'
        ]

def create(self, validated_data):
    images_data = self.context['request'].FILES.getlist('images')
    property_instance = Property.objects.create(**validated_data)
    for image_data in images_data:
        PropertyImage.objects.create(property=property_instance, image=image_data)
    return property_instance