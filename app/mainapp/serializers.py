from rest_framework import serializers

from .functions import *
from .models import *

class ExtendedModelSerializer( serializers.ModelSerializer ):

    def get_field_names( self, declared_fields, info ):
        expanded_fields = super( ExtendedModelSerializer, self ).get_field_names( declared_fields, info )

        if getattr( self.Meta, 'extra_fields', None ):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class DaySerializer( serializers.ModelSerializer ):

    class Meta:
        model = Day
        fields = [ 'number', 'name' ]


class BusinessSerializer( serializers.ModelSerializer ):
    
    class Meta:
        model = Business
        fields = '__all__'


class ServiceSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Service
        fields = [ 'name' ]


class BusinessDaySerializer( serializers.ModelSerializer ):
    days = DaySerializer()

    class Meta:
        model = BusinessToDay
        fields = [ 'days' ]
        

class BusinessServiceSerializer( serializers.ModelSerializer ):
    service = ServiceSerializer()

    class Meta:
        model = BusinessToService
        fields = [ 'service' ]

class ServiceBusinessSerializer( serializers.ModelSerializer ):
    business = BusinessSerializer()

    class Meta:
        model = BusinessToService
        fields = [ 'business' ]


class BusinessInfoSerializer( ExtendedModelSerializer ):

    business_days = BusinessDaySerializer( many=True )
    linked_services = BusinessServiceSerializer( many=True )

    class Meta:
        model = Business
        fields = '__all__'
        extra_fields = [ 'business_days', 'linked_services' ]


class ServicesToBusinessesSerializer( ExtendedModelSerializer ):
    linked_business = ServiceBusinessSerializer( many=True )

    class Meta:
        model = Service
        fields = '__all__'
        extra_fields = [ 'linked_business' ]