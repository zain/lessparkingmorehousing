from random import randint
import json

from django.contrib.gis.geos import GEOSGeometry
from django.http import HttpResponse
import mercantile

from mapdraw.models import ParkingSpot


def new_poly(request):
    if request.method == "POST":
        feature_collection = json.loads(request.body.decode('utf-8'))
        for feature in feature_collection['features']:
            poly = GEOSGeometry(json.dumps(feature['geometry']))
            ParkingSpot.objects.create(poly=poly)
        return HttpResponse('ok', content_type="text/plain")

    return HttpResponse("why don't you POST here", content_type="text/plain")


def next_tile(request):
    # the mission
    ul = (-122.424130, 37.764861)
    br = (-122.404819, 37.749389)
    ZOOM = 20

    ul_tile = mercantile.tile(*ul + (ZOOM,))
    br_tile = mercantile.tile(*br + (ZOOM,))

    x = randint(ul_tile.x, br_tile.x)
    y = randint(ul_tile.y, br_tile.y)
    lng, lat = mercantile.ul(x, y, 20)

    return HttpResponse("[%s, %s]" % (lng, lat), content_type="application/json")
