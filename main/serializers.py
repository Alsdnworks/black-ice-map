"""Markers serializers."""

from rest_framework_gis import serializers

from .models import JoinedLink


class MarkerSerializer(serializers.GeoFeatureModelSerializer):
    """Marker GeoJSON serializer."""

    class Meta:
        """Marker serializer meta class."""
        fields = ("id", "link_id, name")
        geo_field = "location"
        model = JoinedLink