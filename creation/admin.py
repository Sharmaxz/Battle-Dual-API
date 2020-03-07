from django.contrib import admin

from creation.models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'type', 'owner', 'turn')


admin.site.register(Room, RoomAdmin)
