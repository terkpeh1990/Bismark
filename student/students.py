from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from api.paginator import CustomPagination



class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields =['^student_id','^enrolment_certificate']
    ordering_fields = ['student_id','enrolment_certificate']
    ordering = ['-id']