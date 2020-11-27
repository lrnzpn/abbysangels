from django.db import models

# Create your models here.

SERVICES = [
    ( 'Bank', 'Bank' ),
    ( 'Electronics', 'Electronics' ),
    ( 'Fast Food Chain', 'Fast Food Chain' ),
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

class Service( models.Model ):
    name = models.CharField( max_length=127, choices=SERVICES, null=True )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


    class Meta:
        ordering = [ 'name' ]


class Business( models.Model ):

    business_name = models.CharField( max_length=255 )
    address = models.TextField()
    latitude = models.FloatField()
    longtitude = models.FloatField()
    
    representative_name = models.CharField( max_length=255, null=True, blank=True )
    mobile_number = models.CharField( max_length=11, null=True, blank=True )
    telephone_number = models.CharField( max_length=10, null=True, blank=True )
    facebook_link = models.CharField( max_length=127, null=True, blank=True )
    email = models.EmailField( max_length=254 )
    password = models.CharField( max_length=20 )

    services = models.ForeignKey( Service, related_name='business', on_delete=models.SET_NULL, null=True )

    office_hours_start = models.TimeField( null=True, blank=True )
    office_hours_end = models.TimeField( null=True, blank=True)

    weekly_views = models.IntegerField( default=0, blank=True )
    total_views = models.IntegerField( default=0, blank=True )

    def __str__(self):
        return self.business_name
    
    def __repr__(self):
        return self.business_name
    
    def update_views(self, *args, **kwargs):
        self.weekly_views += 1
        self.total_views += 1

        super( Business, self ).save( *args, **kwargs )

    def update_weekly_views(self, *args, **kwargs):
        checkIfEndOfWeek = False

        if checkIfEndOfWeek:
            self.weekly_views = 0
        
        super( Business, self ).save( *args, **kwargs )


    class Meta:
        ordering = [ 'business_name' ]


class BusinessToService( models.Model ):
    business = models.ForeignKey( Business, related_name='linked_services', on_delete=models.CASCADE )
    service = models.ForeignKey( Service, related_name='business_name', on_delete=models.CASCADE )