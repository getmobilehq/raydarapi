from rest_framework import serializers
from .models import InventoryData


class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = InventoryData