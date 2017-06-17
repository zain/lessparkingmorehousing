from django.contrib.gis.geos import Polygon
from django.http import HttpResponse

from mapdraw.models import ParkingSpot


def new_poly(request):
    # if request.method == "POST":
    #     geojson = request.body.decode('utf-8')
    #     ParkingSpot.objects.create(geojson=geojson)
    #     return HttpResponse('ok', content_type="text/plain")
    ext_coords = ((0, 0), (0, 1), (1, 1), (1, 0), (0, 0))
    poly = Polygon(ext_coords)
    ParkingSpot.objects.create(poly=poly)

    return HttpResponse("why don't you POST here", content_type="text/plain")
