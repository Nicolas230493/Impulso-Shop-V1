from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone_number', 'address', 'loyalty_points')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'phone_number', 'address', 'loyalty_points')}),
    )
    list_display = BaseUserAdmin.list_display + ('role', 'phone_number', 'loyalty_points')
    list_filter = BaseUserAdmin.list_filter + ('role',)
