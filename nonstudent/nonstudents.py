from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from api.paginator import CustomPagination



class NonStudentsViewSet(viewsets.ModelViewSet):
    queryset = NonStudents.objects.all()
    serializer_class = NonStudentsSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields =['^id','^work_contract']
    ordering_fields = ['id','work_contract']
    ordering = ['-work_contract']