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
        serializer = self.get_serializer( data=request.data )
        serializer.is_valid( raise_exception=True )

        business_name = serializer.validated_data[ 'business_name' ]
        start_day = serializer.validated_data[ 'business_days' ][0]['days']['number']
        end_day = serializer.validated_data[ 'business_days' ][1]['days']['number']
        service = serializer.validated_data[ 'linked_services' ]

        add_business( serializer.data, start_day, end_day, service )

        return Response( serializer.data )


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