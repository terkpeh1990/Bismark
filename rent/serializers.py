from asyncore import write
from dataclasses import fields
from rest_framework import serializers

import nonstudent
from .models import *
from homeowners.models import Homeowners
from homeowners.serializers import HomeownersSerializer
from student.models import Students
from student.serializers import StudentsRentSerializer
from nonstudent.serializers import NonStudentsRentSerializer
from listing.serializers import ListingsRentSerializer,ListingsSerializer

class RentSerializer(serializers.ModelSerializer):
    listing_id=serializers.PrimaryKeyRelatedField(many=False , queryset = Listings.objects.all())
    student_id = serializers.PrimaryKeyRelatedField(many=False ,read_only=True, allow_null=True)
    nonstudent_id= serializers.PrimaryKeyRelatedField(many=False ,read_only=True, allow_null=True)
    # listing_details = ListingsRentSerializer()
    extra_kwargs = {
            'id': {'read_only': True},
            'nonstudent_id':{'read_only': True},
            'student_id':{'read_only': True},
            'listing_id':{'write_only': True},
            'listing_details':{'read_only': True},
        }
  
    # listing = ListingsSerializer()
  
    class Meta:
        model = Rents
        
        fields = ['id','ref','start_date','end_date','listing_id','nonstudent_id','student_id']

    def create(self, validated_data):

        
        ref = validated_data.get('ref')
       
        try:
            student = Students.objects.get(student_id = ref)
            print('student:', student.student_id)
        except Students.DoesNotExist:
            student = None
            pass
        try:
            nonstudent = NonStudents.objects.get(work_contract=ref)
            print('nonstudent:', nonstudent.work_contract)
        except NonStudents.DoesNotExist:
            nonstudent = None
            pass

        list = Rents.objects.create(**validated_data)
        if student is not None:
            list.student_id = student
        else:
            pass
        if nonstudent is not None:
            list.nonstudent_id = nonstudent
        else:
            pass
        list.save()
        
        return list