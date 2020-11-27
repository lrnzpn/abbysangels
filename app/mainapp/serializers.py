from rest_framework import serializers

from .functions import *
from .models import *


class BusinessSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Business
        fields = '__all__'