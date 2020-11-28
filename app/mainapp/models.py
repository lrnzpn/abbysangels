from django.db import models

# Create your models here.

class Day( models.Model ):
    number = models.IntegerField()
    name = models.CharField( max_length=10 )

    def __str__( self ):
        return self.name

    def __repr__( self ):
        return self.name

    class Meta:
        ordering = [ 'number' ]


class Business( models.Model ):

    business_name = models.CharField( max_length=255 )
    address = models.TextField()
    latitude = models.FloatField()
    longtitude = models.FloatField()
    
    logo = models.FileField( upload_to='images/', null=True, blank=True )
    mobile_number = models.CharField( max_length=11, null=True, blank=True )
    telephone_number = models.CharField( max_length=10, null=True, blank=True )
    website_link = models.CharField( max_length=127, null=True, blank=True )
    email = models.EmailField( max_length=254, null=True )
    password = models.CharField( max_length=20, null=True )

    description = models.TextField( max_length=160, null=True, blank=True )

    office_hours_start = models.TimeField( null=True, blank=True )
    office_hours_end = models.TimeField( null=True, blank=True)

    weekly_views = models.IntegerField( default=0, blank=True )
    total_views = models.IntegerField( default=0, blank=True )

    def __str__( self ):
        return self.business_name
    
    def __repr__( self ):
        return self.business_name
    
    def update_views( self, *args, **kwargs ):
        self.weekly_views += 1
        self.total_views += 1

        super( Business, self ).save( *args, **kwargs )

    def update_weekly_views( self, *args, **kwargs ):
        checkIfEndOfWeek = False

        if checkIfEndOfWeek:
            self.weekly_views = 0
        
        super( Business, self ).save( *args, **kwargs )


    class Meta:
        ordering = [ 'business_name' ]


class Service( models.Model ):
    name = models.CharField( max_length=127 )
    
    def __str__( self ):
        return self.name

    def __repr__( self ):
        return self.name


    class Meta:
        ordering = [ 'name' ]


class BusinessToDay( models.Model ):
    days = models.ForeignKey( Day, related_name='business_name', on_delete=models.CASCADE )
    business = models.ForeignKey( Business, related_name='business_days', on_delete=models.CASCADE )

    def __str__( self ):
        return self.business.business_name + " - " + self.days.name

    def __repr__( self ):
        return self.business.business_name + " - " + self.days.name

    class Meta:
        ordering = [ 'business', 'days' ]


class BusinessToService( models.Model ):
    business = models.ForeignKey( Business, related_name='linked_services', on_delete=models.CASCADE )
    service = models.ForeignKey( Service, related_name='linked_business', on_delete=models.CASCADE )

    def __str__( self ):
        return self.business.business_name + " - " + self.service.name

    def __repr__( self ):
        return self.business.business_name + " - " + self.service.name

    class Meta:
        ordering = [ 'business', 'service' ]