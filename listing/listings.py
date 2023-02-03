from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from api.paginator import CustomPagination

class ListingsViewSet(viewsets.ModelViewSet):
    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields =['^id','owner_id__house_certificate']
    ordering_fields = ['id','home_type','room_type']
    filterset_fields = ['owner_id__house_certificate']
    ordering = ['-id']