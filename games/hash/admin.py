from django.contrib import admin

from games.hash.models import Hash


class HashAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_end', 'turn_count')

admin.site.register(Hash, HashAdmin)
