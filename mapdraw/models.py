from django.contrib.gis.db import models


class ParkingSpot(models.Model):
    poly = models.PolygonField(null=True)


class Tile(models.Model):
    pt = models.PointField()
    times_annotated = models.PositiveIntegerField(default=0)
