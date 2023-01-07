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
    statlv=models.BigIntegerField()

class moct_links(models.Model):
    """A Link with name and location."""
    location = LineStringField()
    fnode_id=models.CharField(max_length=255)
    fnode_name=models.CharField(max_length=255)

class res_links(models.Model):
    """A Link with name and location."""
    min_cost=models.FloatField()
    max_spd=models.IntegerField()
    length=models.FloatField()
    agg_cost=models.FloatField()
    geom=LineStringField()
    path_seq=models.IntegerField()
    road_name=models.CharField(max_length=255)
