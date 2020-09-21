from django.contrib import admin
from .models import Lecture, Attendance


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer_name', 'date', 'level')
    search_fields = ('title', 'lecturer_name')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'get_student', 'get_date')
    search_fields = ('student__userprofile__name',
                     'lecture__title')

    def get_student(self, obj):
        return obj.student.userprofile.name
    get_student.admin_order_field = 'student'
    get_student.short_description = 'Student\'s Name'

    def get_date(self, obj):
        return obj.lecture.date
    get_date.admin_order_field = 'lecture'
    get_date.short_description = 'Date'


admin.site.register(Lecture, LectureAdmin)
admin.site.register(Attendance, AttendanceAdmin)
