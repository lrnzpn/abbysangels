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


class ServiceSerializer( ExtendedModelSerializer ):

    class Meta:
        model = Service
        fields = '__all__'


class BusinessToDaySerializer( serializers.ModelSerializer ):
    days = DaySerializer()
    business = BusinessSerializer()

    class Meta:
        model = BusinessToDay
        fields = '__all__'
        

class BusinessToServiceSerializer( serializers.ModelSerializer ):
    business = BusinessSerializer()
    service = ServiceSerializer( many=True )

    class Meta:
        model = BusinessToService
        fields = '__all__'


class BusinessInfoSerializer( ExtendedModelSerializer ):

    business_days = DaySerializer( many=True )
    linked_services = ServiceSerializer( many=True )

    class Meta:
        model = Business
        fields = '__all__'
        extra_fields = [ 'business_days', 'linked_services' ]


class ServicesToBusinessesSerializer( ExtendedModelSerializer ):
    linked_businesses = BusinessSerializer( many=True )

    class Meta:
        model = Service
        fields = '__all__'
        extra_fields = [ 'linked_businesses' ]