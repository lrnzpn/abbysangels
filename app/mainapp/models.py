from django.db import models

from collectionfield.models import CollectionField
# Create your models here.

SERVICES = [
    ( 'Bank', 'Bank' ),
    ( 'Electronics', 'Electronics' ),
    ( 'Gas Station', 'Gas Station' ),
    ( 'Grocery', 'Grocery' ),
    ( 'Hardware and Construction Materials', 'Hardware and Construction Materials' ),
    ( 'Hospital', 'Hospital' ),
    ( 'Payment Gateway', 'Payment Gateway' ),
    ( 'Pharmacy', 'Pharmacy' ),
    ( 'Restaurants', 'Restaurants' ),
    ( 'Supermarket', 'Supermarket' ),
    ( 'Utility Company', 'Utility Company' ),
]


class Location( models.Model ):

    business_name = models.CharField( max_length=255 )
    address = models.TextField()
    latitude = models.FloatField()
    longtitude = models.FloatField()
    
    representative_name = models.CharField( max_length=255, null=True, blank=True )
    mobile_number = models.CharField( max_length=11 )
    telephone_number = models.CharField( max_length=10 )

    services = CollectionField( choices=SERVICES )

    office_hours = models.CharField( max_length=20 )