from django.http import HttpResponse

from mapdraw.models import ParkingSpot


def new_parking_spot(request):
    ParkingSpot.objects.create(shape='hi')

    return HttpResponse('ok', content_type="text/plain")
