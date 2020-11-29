from django.contrib.auth import login, authenticate
from django.shortcuts import render

from .models import *
from .functions import *
from .serializers import *

from rest_framework import viewsets, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class BusinessViewSet ( viewsets.ModelViewSet ):
    queryset = Business.objects.all()
    serializer_class = BusinessInfoSerializer

    def create( self, request, *args, **kwargs ):

        add_business( request.data )

        return Response( request.data )


class DayViewSet( viewsets.ModelViewSet ):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class ServiceViewSet( viewsets.ModelViewSet ):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceToBusinessesViewSet( viewsets.ModelViewSet ):
    queryset = Service.objects.all()
    serializer_class = ServicesToBusinessesSerializer


class LoginAPI( APIView ):
    
    def post( self, request, format=None ):
        serializer = AuthTokenSerializer( data=request.data )
        serializer.is_valid( raise_exception=True )
        user = serializer.validated_data['user']
        login( request, user )
        return super( LoginAPI, self ).post( request, format=None )