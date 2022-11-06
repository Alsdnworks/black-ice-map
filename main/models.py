from django.db import models
from django.db import connection
# Create your models here.
"""Markers models."""

from django.contrib.gis.db.models import *

class Marker(models.Model):
    """A marker with name and location."""
    name = models.CharField(max_length=255)
    location = PointField()

class Link(models.Model):
    """A Link with name and location."""
    link_id = models.CharField(max_length=255)
    location = MultiPolygonField()

class JoinedLink(models.Model):
    """A Link with name and location."""
    link_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = MultiPolygonField()    