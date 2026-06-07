from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'get_full_name', 'role', 'phone', 'is_staff', 'is_active', 'created_at')
    list_filter = ('role', 'is_staff', 'is_active', 'created_at')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    ordering = ('-created_at',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone', 'address', 'profile_picture')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'Full Name'

admin.site.register(CustomUser, CustomUserAdmin)