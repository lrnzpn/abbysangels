from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register( Day )
admin.site.register( Service )
admin.site.register( Business )
admin.site.register( BusinessToDay )
admin.site.register( BusinessToService )