from django.db import models


class ParkingSpot(models.Model):
    shape = models.TextField()
