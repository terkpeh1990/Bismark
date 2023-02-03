from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class StudentsSerializer(serializers.ModelSerializer):
    # extra_kwargs = {
    #         'id': {'read_only': True}
    #     }
    class Meta:
        model = Students
        fields =['student_id','enrolment_certificate']



class StudentsRentSerializer(serializers.ModelSerializer):
    extra_kwargs = {
            # 'id': {'read_only': True},
            'student_id': {'read_only': True},
            'enrolment_certificate': {'read_only': True}
        }
    class Meta:
        model = Students
        fields =['student_id','enrolment_certificate']