from django.db import models
from homeowners.models import Homeowners
from simple_history.models import HistoricalRecords
from auth_account.models import User
from listing.models import Listings
from student.models import Students
from nonstudent.models import NonStudents


# Create your models here.
class Rents(models.Model):
    ref = models.CharField(max_length=250,null=True, blank=True)
    listing_id =models.ForeignKey(Listings, on_delete=models.CASCADE,null=True, blank=True)
    student_id =models.ForeignKey(Students, on_delete=models.CASCADE,null=True, blank=True)
    nonstudent_id =models.ForeignKey(NonStudents, on_delete=models.CASCADE,null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.ref
