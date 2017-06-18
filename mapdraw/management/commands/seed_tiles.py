from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
import mercantile

from mapdraw.models import Tile


class Command(BaseCommand):
    def handle(self, *args, **options):
        # the mission
        ul = (-122.424130, 37.764861)
        br = (-122.404819, 37.749389)
        ZOOM = 19

        ul_tile = mercantile.tile(*ul + (ZOOM,))
        br_tile = mercantile.tile(*br + (ZOOM,))

        for x in range(ul_tile.x, br_tile.x + 1):
            for y in range(ul_tile.y, br_tile.y + 1):
                lng, lat = mercantile.ul(x, y, ZOOM)
                Tile.objects.get_or_create(pt=Point(lng, lat))
