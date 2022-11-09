"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import JoinedLink
from .serializers import MarkerSerializer

class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""
    from django.db import connection
    cursor=connection.cursor()
    ##########부등호를 바꿔서 6시간 이상인 것들을 삭제하고, 6시간 이하인 것들을 가져온다.----오류!!---->해결 11/9
    cursor.execute("DELETE from public.main_marker where (now() - date) > interval '6 hour';")
    cursor.execute("TRUNCATE main_joinedlink;")
    cursor.execute("INSERT INTO main_joinedlink overriding system value select nextval('main_joinedlink_id_seq'), main_link.location, main_marker.stat from main_link,main_marker  where ST_CONTAINS(main_link.location, main_marker.location) ;")
    connection.close()
    queryset=JoinedLink.objects.all()
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    serializer_class = MarkerSerializer
