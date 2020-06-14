from django.contrib import admin
from .models import WaitlistEntry


class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at')
    search_fields = ('first_name', 'last_name')


admin.site.register(WaitlistEntry, WaitlistEntryAdmin)
