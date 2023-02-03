from dataclasses import field
from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class HomeownersSerializer(serializers.ModelSerializer):
    extra_kwargs = {
            'id': {'read_only': True}
        }
    class Meta:
        model = Homeowners
        fields =['id','house_certificate']


class HomeownersListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeowners
        fields =['id']

class HomeownersRentSerializer(serializers.ModelSerializer):
    extra_kwargs = {
            'id': {'read_only': True},
            'house_certificate': {'read_only': True},
            'house_certificate':{'allow_null=True':True}
        }
    class Meta:
        model = Homeowners
        fields =['id','house_certificate']