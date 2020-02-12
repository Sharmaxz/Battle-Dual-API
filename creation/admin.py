from django.contrib import admin

from creation.models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'game', 'type')


admin.site.register(Room, RoomAdmin)
