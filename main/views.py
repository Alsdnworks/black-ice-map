import json
from django.core.serializers import serialize
#from .models import JoinedLink
#from .models import moct_links
from .models import res_links
from django.views.generic.base import TemplateView
from django.db import connection

class MarkersMapView(TemplateView):
    """Markers map view."""
    template_name = "map.html"
    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        search_text_s = self.request.GET.get('search_text1')
        search_text_e = self.request.GET.get('search_text2')
        if search_text_s == None:
            # TODO: set default value 이거 어떻게 할지 고민좀
            search_text_s = '군포역'
            search_text_e = '강원대'
        cursor = connection.cursor()
        cursor.execute(f'''select MAX(l.fnode_id::bigint) from main_moct_links as l where l.fnode_name like '{search_text_s}%';''')
        start=cursor.fetchall()
        cursor.execute(f'''select MAX(l.fnode_id::bigint) from main_moct_links as l where l.fnode_name like '{search_text_e}%';''')
        end=cursor.fetchall()
        query=f"""
        truncate main_res_links;
        INSERT INTO main_res_links (road_name, max_spd, length, min_cost, geom, path_seq, agg_cost)
        SELECT l.road_name, l.max_spd, l.length, l.min_cost, l.geom, d.path_seq, d.agg_cost
        FROM moct_link l
        INNER JOIN (
            SELECT edge::varchar(10) AS edge, seq, path_seq, node, cost, agg_cost
            FROM pgr_dijkstra(
                'SELECT link_id::bigint as id, 
                    f_node::bigint as source, 
                    t_node::bigint as target, 
                    length::bigint as cost
                FROM moct_link',
                {str(start[0][0])}::bigint,
                {str(end[0][0])}::bigint
            )
        ) AS d
        ON l.link_id = d.edge;
        """
        cursor.execute(query)
        cursor.execute('''select max(agg_cost)/1000 as "cost(km)" from main_res_links;''')
        cost_l=cursor.fetchall()
        cursor.execute('''select sum(min_cost)/60 as "cost(minute)" from main_res_links;''')
        cost_t=cursor.fetchall()
        connection.commit()
        connection.close()
        context["time"] = int(cost_t[0][0])
        context["cost"] = int(cost_l[0][0])
        context["markers"] = json.loads(serialize("geojson", res_links.objects.all()))
        return context
        #except:
        #    search_text = self.request.GET['search_text']
        #    context["statuss"] = json.loads(serialize("geojson", moct_links.objects.filter(fnode_name__icontains=search_text)))
        #    context["markers"] = ''
        #    return context
        #except:
        #    context["statuss"] = ''
        #    context["markers"] = json.loads(serialize("geojson", JoinedLink.objects.all()))
        #    return context