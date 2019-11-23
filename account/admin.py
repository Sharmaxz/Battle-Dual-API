from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


class MyUserAdmin(UserAdmin):
    search_fields = ('email', 'nickname', 'first_name', 'date_joined')
    list_display = ('nickname', 'email', 'first_name', 'is_staff')
    ordering = ('nickname', 'email', 'date_joined')
    fieldsets = (
        (None, {'fields': ('nickname', 'email', 'password')}),
        ("Personal information", {'fields': ('first_name', 'last_name', 'birthdate')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ("Activity", {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, MyUserAdmin)
