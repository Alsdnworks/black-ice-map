"""Markers serializers."""

from rest_framework_gis import serializers

from .models import JoinedLink
from .models import moct_links

class MarkerSerializer(serializers.GeoFeatureModelSerializer):
    """Marker GeoJSON serializer."""
    class Meta:
        """Marker serializer meta class."""
        fields = ("id")
        geo_field = "location"
        LV="statLV"
        model = JoinedLink
        