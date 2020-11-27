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
    facebook_link = models.CharField( max_length=127 )

    services = CollectionField( choices=SERVICES )

    office_hours = models.CharField( max_length=20 )

    weekly_views = models.IntegerField()
    total_views = models.IntegerField()

    def __str__(self):
        return self.business_name
    
    def __repr__(self):
        return self.business_name
    
    def update_views(self, *args, **kwargs):
        self.weekly_views += 1
        self.total_views += 1

        super( Location, self ).save( *args, **kwargs )

    
    class Meta:
        ordering = [ 'business_name' ]
