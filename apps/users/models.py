from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('CLIENT', 'Cliente'),
        ('DRIVER', 'Repartidor / Delivery'),
        ('ADMIN', 'Administrador'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CLIENT')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    loyalty_points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
