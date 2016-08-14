from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from reversion.admin import VersionAdmin
from django.contrib import admin
from . import models


class UserAdmin(VersionAdmin, BaseUserAdmin):
    list_filter = ('is_active', 'is_superuser', 'last_login')
    list_display = ('username', 'email', 'last_login', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username', )

    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        ('Credentials', {
            'fields': (
                'username',
                'email',
                'password',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        ('Information', {
            'fields': (
                'date_joined',
                'last_login',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
