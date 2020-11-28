from django.shortcuts import render

from .models import *
from .functions import *
from .serializers import *

from rest_framework import viewsets

# Create your views here.

class BusinessViewSet( viewsets.ModelViewSet ):
    queryset = Business.objects.all()
    serializer_class = BusinessInfoSerializer


class DayViewSet( viewsets.ModelViewSet ):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class ServiceViewSet( viewsets.ModelViewSet ):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceToBusinessesViewSet( viewsets.ModelViewSet ):
    queryset = Service.objects.all()
    serializer_class = ServicesToBusinessesSerializer