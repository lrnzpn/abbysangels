from django.shortcuts import render

from .models import *
from .functions import *
from .serializers import *

from rest_framework import viewsets

# Create your views here.

class LocationViewSet( viewsets.ModelViewSet ):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer