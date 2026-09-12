from django.db import models
from django.conf import settings
from apps.orders.models import Order

class Delivery(models.Model):
    STATUS_CHOICES = [
        ('ASSIGNED', 'Asignado'),
        ('PICKED_UP', 'En retiro'),
        ('IN_TRANSIT', 'En camino'),
        ('DELIVERED', 'Entregado'),
        ('FAILED', 'Fallido'),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery')
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        limit_choices_to={'role': 'DRIVER'}, 
        null=True, 
        blank=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ASSIGNED')
    pickup_address = models.TextField()
    delivery_address = models.TextField()
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    estimated_delivery_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery for Order {self.order.id}"

class DeliveryLocationHistory(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='location_history')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location at {self.timestamp} for {self.delivery}"
