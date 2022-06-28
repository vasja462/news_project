from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email',)
    list_filter = ('email',)
    fieldsets = (
        ('Personal Information', {'fields': ('email',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', )}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

