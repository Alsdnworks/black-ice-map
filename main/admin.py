"""Markers admin."""

from django.contrib.gis import admin

from .models import Marker
from .models import Link


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")
@admin.register(Link)
class LinkAdmin(admin.OSMGeoAdmin):
    """Link admin."""

    list_display = ("link_id", "location")
