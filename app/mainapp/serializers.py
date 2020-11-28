from rest_framework import serializers

from .functions import *
from .models import *

class ServiceSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Service
        fields = '__all__'


class BusinessSerializer( serializers.ModelSerializer ):
    
    services = ServiceSerializer( many=True )

    class Meta:
        model = Business
        fields = '__all__'


class BusinessToServiceSerializer( serializers.ModelSerializer ):
    business = BusinessSerializer()
    service = ServiceSerializer( many=True )