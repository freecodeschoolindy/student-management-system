from django.db import models
from django.contrib.auth import get_user_model


class AbstractTableMeta(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.DO_NOTHING,
                                   related_name='+')
    modified_by = models.ForeignKey(get_user_model(),
                                    on_delete=models.DO_NOTHING,
                                    related_name='+')

    class Meta:
        abstract = True
