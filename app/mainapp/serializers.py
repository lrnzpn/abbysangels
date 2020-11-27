from rest_framework import serializers

from .functions import *
from .models import *


class LocationSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Location
        fields = '__all__'