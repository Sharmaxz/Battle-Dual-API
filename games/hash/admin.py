from django.contrib import admin

from games.hash.models import Hash
from games.hash.models import Item


class HashAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('type',)


admin.site.register(Hash, HashAdmin)
admin.site.register(Item, ItemAdmin)
