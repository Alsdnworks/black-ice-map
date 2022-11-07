from django.db import models
from django.contrib.gis.db.models import *
# Create your models here.
"""Markers models."""


class Marker(models.Model):
    """A marker with name and location."""
    name = models.CharField(max_length=255)
    location = PointField()
    stat=models.BigIntegerField()
    date=models.DateTimeField()

class Link(models.Model):
    """A Link with name and location."""
    link_id = models.CharField(max_length=255)
    location = MultiPolygonField()

    
class JoinedLink(models.Model):
    """A Link with name and location."""
    location = MultiPolygonField()    
    statLV=models.BigIntegerField()