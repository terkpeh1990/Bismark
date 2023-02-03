from django.contrib.auth.models import AbstractUser
from django.db import models
from student.models import Students
from nonstudent.models import NonStudents
from homeowners.models import Homeowners

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    verification_card =models.CharField(max_length=200)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE,null=True, blank=True)
    nonstudent_id = models.ForeignKey(NonStudents, on_delete=models.CASCADE,null=True, blank=True)
    homeowners_id =models.ForeignKey(Homeowners, on_delete=models.CASCADE,null=True, blank=True)
    username =None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


