from django.contrib import admin
from mapdraw.models import ParkingSpot


class ParkingSpotAdmin(admin.ModelAdmin):
    pass
admin.site.register(ParkingSpot, ParkingSpotAdmin)
