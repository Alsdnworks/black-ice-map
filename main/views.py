from django.shortcuts import render
import json
from django.core.serializers import serialize
from .models import JoinedLink
from django.views.generic.base import TemplateView

class MarkersMapView(TemplateView):
    """Markers map view."""
    template_name = "map.html"
    def get_context_data(self, **kwargs):
        """Return the view context data."""
        from django.db import connection
        cursor=connection.cursor()
        ##########부등호를 바꿔서 6시간 이상인 것들을 삭제하고, 6시간 이하인 것들을 가져온다.----오류!!
        
        cursor.execute("DELETE from public.main_marker where (now() - date) < interval '6 hour'; TRUNCATE main_joinedlink; INSERT INTO main_joinedlink overriding system value select main_link.id+1, main_link.location, main_marker.stat from main_link,main_marker  where ST_CONTAINS(main_link.location, main_marker.location) ;")
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", JoinedLink.objects.all()))
        connection.close() 
    
        return context