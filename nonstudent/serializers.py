from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class NonStudentsSerializer(serializers.ModelSerializer):
    # extra_kwargs = {
    #         'id': {'read_only': True}
    #     }
    class Meta:
        model = NonStudents
        fields =['work_contract']


class NonStudentsRentSerializer(serializers.ModelSerializer):
    extra_kwargs = {
            # 'id': {'read_only': True},
            'work_contract': {'read_only': True}
        }
    class Meta:
        model = NonStudents
        fields =['work_contract']