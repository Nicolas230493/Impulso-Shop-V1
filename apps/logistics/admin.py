from django.contrib import admin
from .models import Delivery, DeliveryLocationHistory

class DeliveryLocationHistoryInline(admin.TabularInline):
    model = DeliveryLocationHistory
    extra = 0
    readonly_fields = ('timestamp',)

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    inlines = [DeliveryLocationHistoryInline]
    list_display = ('order', 'driver', 'status', 'created_at')
    list_filter = ('status', 'driver')
    search_fields = ('order__id', 'driver__username')
