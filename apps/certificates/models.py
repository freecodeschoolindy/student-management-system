from django.db import models

from apps.utils.models import AbstractTableMeta


class Certificate(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
