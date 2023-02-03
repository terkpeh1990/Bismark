from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from api.paginator import CustomPagination



class HomeownersViewSet(viewsets.ModelViewSet):
    queryset = Homeowners.objects.all()
    serializer_class = HomeownersSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields =['^id','^house_certificate']
    ordering_fields = ['id','house_certificate']
    ordering = ['-id']