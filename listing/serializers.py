from rest_framework import serializers
from .models import *
from homeowners.models import Homeowners
from homeowners.serializers import HomeownersSerializer,HomeownersRentSerializer
from drf_writable_nested import WritableNestedModelSerializer
from auth_account.serializers import UserUseSerializer



class ListingsSerializer(serializers.ModelSerializer):
    # owner_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True)
    owner_id = HomeownersSerializer()
    # owner = HomeownersSerializer(read_only = True)
    extra_kwargs = {
            'id': {'read_only': True}
        }
    class Meta:
        model = Listings
        
        exclude = ['created_at','updated_at']
    
    def create(self, validated_data):
        owner_data = validated_data.pop('owner_id')
        print(owner_data)
        try:
            owner = Homeowners.objects.get(house_certificate=owner_data['house_certificate'])
        except Homeowners.DoesNotExist:
            raise serializers.ValidationError("Incorrent house certifiacte or home owner does not exist")
        list = Listings.objects.create(**validated_data)
        list.owner_id =owner
        list.save()
        
        return list

class ListingsRentSerializer(serializers.ModelSerializer):
    
    owner_id = HomeownersRentSerializer()
   
    extra_kwargs = {
            'id': {'read_only': True},
            'owner_id': {'read_only': True},
            'home_type':{'read_only': True},
            'room_type':{'read_only': True},
            'total_occupancy':{'read_only': True},
            'total_bedrooms':{'read_only': True},
            'total_bathrooms':{'read_only': True},
            'summary':{'read_only': True},
            'address':{'read_only': True},
            'furnished':{'read_only': True},
            'price':{'read_only': True},
            'published_at':{'read_only': True},
        }
    class Meta:
        model = Listings
        
        exclude = ['created_at','updated_at']

   
    class Meta:
        model = Listings
        
        fields = ['id','owner_id']
    
    
