from django.contrib.gis.geos import Polygon
from django.http import HttpResponse

from mapdraw.models import ParkingSpot


def new_parking_spot(request):
    ext_coords = ((0, 0), (0, 1), (1, 1), (1, 0), (0, 0))
    poly = Polygon(ext_coords)
    ParkingSpot.objects.create(poly=poly)

    return HttpResponse('ok', content_type="text/plain")
