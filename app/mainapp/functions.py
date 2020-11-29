from .models import *
from datetime import datetime

import base64
import mimetypes
import os
import sys

def img_to_data( path ):
    """Convert a file (specified by a path) into a data URI."""
    if not os.path.exists(path):
        raise FileNotFoundError
    mime, _ = mimetypes.guess_type(path)
    with open(path, 'rb') as fp:
        data = fp.read()
        data64 = u''.join(base64.encodestring(data).splitlines())
        return u'data:%s;base64,%s' % (mime, data64)


def add_business( business_data ):
    business_to_check = Business.objects.filter( business_name=business_data[ 'business_name' ] )

    start_day = business_data[ 'business_days' ][0]
    end_day = business_data[ 'business_days' ][1]
    services = business_data[ 'linked_services' ]

    if business_to_check.exists():
        print( "Business name already taken. Please input a new one." )
        return False

    business_to_process = Business.objects.create( 
        business_name = business_data['business_name'],
        address = business_data['address'],
        latitude = business_data['latitude'],
        longitude = business_data['longitude'],
        logo = business_data['logo'],
        mobile_number = business_data['mobile_number'],
        telephone_number = business_data['telephone_number'],
        website_link = business_data['website_link'],
        email = business_data['email'],
        password = business_data['password'],
        description = business_data['description'],
        office_hours_start = business_data['office_hours_start'],
        office_hours_end = business_data['office_hours_end']
        )

    BusinessToDay.objects.create(
            days=Day.objects.get( number=start_day),
            business=business_to_process
        )
    BusinessToDay.objects.create(
            days=Day.objects.get( number=end_day ),
            business=business_to_process
        )

    for i in services:
        print(i)
        service = Service.objects.get( name=i )

        BusinessToService.objects.create(
            business=business_to_process,
            service=service
        )