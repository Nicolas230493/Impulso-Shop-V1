from rest_framework import serializers
from .models import Delivery, DeliveryLocationHistory
from apps.orders.serializers import OrderSerializer

class DeliveryLocationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLocationHistory
        fields = ['latitude', 'longitude', 'timestamp']

class DeliverySerializer(serializers.ModelSerializer):
    location_history = DeliveryLocationHistorySerializer(many=True, read_only=True)
    order = OrderSerializer(read_only=True)
    
    class Meta:
        model = Delivery
        fields = ['id', 'order', 'driver', 'status', 'pickup_address', 'delivery_address', 
                  'current_latitude', 'current_longitude', 'estimated_delivery_time', 
                  'created_at', 'updated_at', 'location_history']
