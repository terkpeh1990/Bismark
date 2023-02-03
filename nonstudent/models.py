from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class NonStudents(models.Model):
 
    work_contract = models.CharField(max_length=100,primary_key=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    history = HistoricalRecords()

    def __str__(self):
        return self.work_contract