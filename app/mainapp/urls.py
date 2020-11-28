from django.contrib import admin
from django.urls import path, include

from .models import *
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register( r'businesses', BusinessViewSet)
router.register( r'days', DayViewSet)



urlpatterns = [
    path( '', include(router.urls) ),
]