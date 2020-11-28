from django.shortcuts import render

from .models import *
from .functions import *
from .serializers import *

from rest_framework import viewsets

# Create your views here.

class BusinessViewSet( viewsets.ModelViewSet ):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer