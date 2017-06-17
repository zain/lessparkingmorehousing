from django.contrib.gis.db import models


class ParkingSpot(models.Model):
    poly = models.PolygonField(null=True)
