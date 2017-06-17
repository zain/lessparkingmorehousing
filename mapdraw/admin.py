from django.contrib.gis import admin
from mapdraw.models import ParkingSpot


class ParkingSpotAdmin(admin.GeoModelAdmin):
    pass
admin.site.register(ParkingSpot, ParkingSpotAdmin)
