from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'level', 'required')
    list_filter = ('level',)


admin.site.register(Project, ProjectAdmin)
