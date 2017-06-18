from random import randint
import json

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from django.db.models import F, Avg
from django.http import HttpResponse
import mercantile

from mapdraw.models import ParkingSpot, Tile


def new_poly(request):
    if request.method != "POST":
        return HttpResponse("why don't you POST here", content_type="text/plain")

    payload = json.loads(request.body.decode('utf-8'))

    feature_collection = payload['geojson']
    for feature in feature_collection['features']:
        poly = GEOSGeometry(json.dumps(feature['geometry']))
        ParkingSpot.objects.create(poly=poly)

    tile_id = payload['tile_id']
    Tile.objects.filter(id=tile_id).update(times_annotated=F('times_annotated')+1)

    return HttpResponse('ok', content_type="text/plain")


def next_tile(request):
    avg_annotations = Tile.objects.aggregate(Avg('times_annotated'))['times_annotated__avg']
    tile_set = Tile.objects.filter(times_annotated__lte=avg_annotations)

    if 'close_to' in request.GET and request.GET['close_to'] != 'null':
        in_tile = Tile.objects.get(id=int(request.GET['close_to']))
        tile_set = tile_set.annotate(distance=Distance('pt', in_tile.pt)).order_by('distance')
        tile = tile_set[0]
    else:
        tile = tile_set[randint(0, tile_set.count())]

    output = {
        'lat': tile.pt.y,
        'lng': tile.pt.x,
        'tile_id': tile.id,
        'existing': {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": json.loads(spot.poly.geojson),
                } for spot in ParkingSpot.objects.filter(poly__distance_lte=(tile.pt, D(mi=1)))
            ]
        },
    }

    return HttpResponse(json.dumps(output), content_type="application/json")
