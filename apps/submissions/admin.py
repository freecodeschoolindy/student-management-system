from django.contrib import admin

from .models import StudentSubmission


class StudentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('get_student', 'get_project',
                    'approved', 'created_at')
    # list_filter = ('project__title',)
    search_fields = ('student__userprofile__name',)

    def get_project(self, obj):
        return obj.project.title
    get_project.admin_order_field = 'project'
    get_project.short_description = 'Project Title'

    def get_student(self, obj):
        return obj.student.userprofile.name
    get_student.admin_order_field = 'student'
    get_student.short_description = 'Student\'s Name'


admin.site.register(StudentSubmission, StudentSubmissionAdmin)
