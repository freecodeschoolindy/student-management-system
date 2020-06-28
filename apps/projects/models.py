from django.db import models

from apps.utils.models import AbstractTableMeta


class Project(AbstractTableMeta, models.Model):
    title = models.CharField(max_length=100)
    desription = models.TextField(blank=True, default='')
    url = models.CharField(max_length=255)
    level = models.IntegerField(choices=((1, 'Level 1'), (2, 'Level 2')),
                                default=1)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.title
