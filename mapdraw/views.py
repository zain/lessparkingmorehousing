from django.http import HttpResponse

from mapdraw.models import ParkingSpot


def new_poly(request):
    if request.method == "POST":
        geojson = request.body.decode('utf-8')
        ParkingSpot.objects.create(geojson=geojson)
        return HttpResponse('ok', content_type="text/plain")
    return HttpResponse("why don't you POST here", content_type="text/plain")
