from rest_framework import serializers
from .models import CargoRequest

class CargoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoRequest
        fields = '__all__'