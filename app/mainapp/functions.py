from .models import *
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


def add_business( business_name, start_day, end_day, services ):
    business_to_process = Business.objects.get( business_name=business_name )

    for i in range( start_day, end_day + 1 ):
        day = Day.objects.get( number=i )

        BusinessToDay.objects.create(
            days=day,
            business=business_to_process
        )
    
    for i in services:
        service = Service.objects.get( name=i )

        BusinessToService.objects.create(
            business=business_to_process,
            service=service
        )