from django.contrib import admin
from .models import PointLocations, AirQualityReadings
# Register your models here.
admin.site.register(PointLocations)
admin.site.register(AirQualityReadings)