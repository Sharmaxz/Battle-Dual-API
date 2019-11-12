from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import user


class MyUserAdmin(UserAdmin):
    search_fields = ('email',)
    list_display = ('email', 'name', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ("Personal information", {'fields': ('name',)}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ("Activity", {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(user, MyUserAdmin)
