from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from webapp.models import Region, Area, Plot


@admin.register(Region)
class RegionAdmin(LeafletGeoAdmin):
    list_display = ("name", "coordinates")


@admin.register(Area)
class AreaAdmin(LeafletGeoAdmin):
    list_display = ("name", "coordinates")


@admin.register(Plot)
class PlotAdmin(LeafletGeoAdmin):
    list_display = ("name", "coordinates")
