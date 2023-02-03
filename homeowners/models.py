from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class Homeowners(models.Model):
    house_certificate= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.house_certificate