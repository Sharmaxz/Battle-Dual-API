from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


class MyUserAdmin(UserAdmin):
    search_fields = ('nickname', 'email',)
    list_display = ('nickname', 'email', 'first_name', 'is_staff')
    ordering = ('nickname',)
    fieldsets = (
        (None, {'fields': ('username', 'nickname', 'password')}),
        ("Personal information", {'fields': ('first_name', 'last_name')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ("Activity", {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, MyUserAdmin)