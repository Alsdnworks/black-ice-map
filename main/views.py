import json
from django.core.serializers import serialize
from .models import JoinedLink
from .models import moct_links
from django.views.generic.base import TemplateView
from django.shortcuts import render
class MarkersMapView(TemplateView):
    """Markers map view."""
    template_name = "map.html"
    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", JoinedLink.objects.all()))
        return context

def search_view(request):
    """Return the view context data."""
    search_text = request.GET['search_text']
    if search_text is not None and search_text != u"":
        search_text = request.GET['search_text']
    res= json.loads(serialize("geojson", moct_links.objects.filter(fnode_name__icontains=search_text)))
    return render(request, 'map.html', {'statuss':res})
