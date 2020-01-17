from django.contrib import admin
from .models import Item


# admin.site.register(Item)
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_published']
    list_display_links = ['name']
    list_filter = ['is_published', 'updated_at']
    search_fields = ['name']

    def short_desc(self, item):
        return item.desc[:20]