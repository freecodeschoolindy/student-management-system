from django.contrib import admin

from .models import Volunteer, VolunteerHours


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


class VolunteerHoursAdmin(admin.ModelAdmin):
    list_display = ('get_volunteer', 'start', 'end')
    search_fields = ('volunteer__first_name', 'volunteer__last_name')

    def get_volunteer(self, obj):
        return obj.volunteer.full_name
    get_volunteer.admin_order_field = 'volunteer'
    get_volunteer.short_description = 'Volunteer\'s Name'


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(VolunteerHours, VolunteerHoursAdmin)
