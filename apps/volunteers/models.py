from django.db import models


class Volunteer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    hours_available = models.TextField(blank=True, default='')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class VolunteerHours(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'VolunteerHours'
