from django.db import models


class ParkingSpot(models.Model):
    geojson = models.TextField()
