from rest_framework import serializers
from .models import Farm, Crop

class CropSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)

    class Meta:
        model = Crop
        fields = ['id', 'farm', 'farm_name', 'type', 'growth_stage', 
                 'water_requirements', 'fertilizer_requirements']
        
    def validate_water_requirements(self, value):
        if value < 0:
            raise serializers.ValidationError("Water requirements cannot be negative")
        return value

    def validate_fertilizer_requirements(self, value):
        if value < 0:
            raise serializers.ValidationError("Fertilizer requirements cannot be negative")
        return value

class FarmSerializer(serializers.ModelSerializer):
    crops = CropSerializer(many=True, read_only=True)
    crops_count = serializers.IntegerField(source='crops.count', read_only=True)

    class Meta:
        model = Farm
        fields = ['id', 'name', 'location', 'area', 'crops', 'crops_count']

    def validate_area(self, value):
        if value <= 0:
            raise serializers.ValidationError("Area must be greater than 0")
        return value
