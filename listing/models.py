from django.db import models
from homeowners.models import Homeowners
from simple_history.models import HistoricalRecords
from auth_account.models import User


# Create your models here.
class Listings(models.Model):
    home_type = models.CharField(max_length=250)
    room_type = models.CharField(max_length=250)
    total_occupancy = models.IntegerField()
    total_bedrooms = models.PositiveIntegerField()
    total_bathrooms = models.IntegerField()
    summary =models.CharField(max_length=250)
    address =models.CharField(max_length=250)
    furnished =models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    published_at = models.DateTimeField(auto_now_add=True)
    owner_id =models.ForeignKey(Homeowners, on_delete=models.CASCADE,null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10,null=True,blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.summary