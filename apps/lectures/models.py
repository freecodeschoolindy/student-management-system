from django.db import models
from django.contrib.auth import get_user_model

from apps.utils.models import AbstractTableMeta


class Lecture(AbstractTableMeta, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='',
                                     blank=True)
    date = models.DateField()
    duration = models.IntegerField(help_text='Enter number of hours')
    slides_url = models.CharField(max_length=255)
    level = models.IntegerField(choices=((1, 'Level 1'), (2, 'Level 2')),
                                default=1)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Attendance(AbstractTableMeta, models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
