from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Delivery, DeliveryLocationHistory
from .serializers import DeliverySerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DeliverySerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.role == 'ADMIN':
            return Delivery.objects.all()
        elif user.role == 'DRIVER':
            return Delivery.objects.filter(driver=user)
        else:
            return Delivery.objects.filter(order__user=user)

    @action(detail=True, methods=['post'])
    def update_location(self, request, pk=None):
        delivery = self.get_object()
        user = request.user
        
        # Check permissions
        if not (user.is_staff or user.role == 'ADMIN' or delivery.driver == user):
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
            
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        
        if latitude is None or longitude is None:
            return Response({'error': 'latitude and longitude required'}, status=status.HTTP_400_BAD_REQUEST)
            
        delivery.current_latitude = latitude
        delivery.current_longitude = longitude
        delivery.save()
        
        DeliveryLocationHistory.objects.create(
            delivery=delivery,
            latitude=latitude,
            longitude=longitude
        )
        
        return Response(DeliverySerializer(delivery).data)

    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        delivery = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in [choice[0] for choice in Delivery.STATUS_CHOICES]:
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
            
        delivery.status = new_status
        delivery.save()
        
        return Response(DeliverySerializer(delivery).data)
