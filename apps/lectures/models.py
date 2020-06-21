from django.db import models

from apps.utils.models import Timestamps


class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='',
                                     blank=True)
    date = models.DateField()
    duration = models.IntegerField(help_text='Enter number of hours')
    slides_url = models.CharField(max_length=255)
    level = models.IntegerField(choices=((1, 'Level 1'), (2, 'Level 2')),
                                default=1)
    is_required = models.BooleanField(default=True)
