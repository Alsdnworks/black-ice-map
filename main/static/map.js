
var container = L.DomUtil.get('map');
if(container != null){
  container._leaflet_id = null;
}

var attribution =
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
    var map = L.map("map");
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: attribution,
    }).addTo(map);
    map.fitWorld();

if (markers!=''){
    var line_feature =L.geoJSON(markers,{
        onEachFeature: function(feature,layer){
            //show properties when click on the line
                    layer.bindPopup(
                        "<h2>도로명: "+feature.properties.road_name+"</h2>"+
                        "<h3>도로길이(m): "+parseInt(feature.properties.length)+"</h3>"+
                        "<h3>최대속도(km/h): "+parseInt(feature.properties.max_spd)+"</h3>"+
                        "<h3>최소 통과시간(초): "+parseInt(feature.properties.min_cost)+"</h3>"
                    );
        }
    }).addTo(map);
    map.fitBounds(line_feature.getBounds(), { padding: [100, 100] });
}
else {
    if (markers!=''){
    var mark_feature = L.geoJSON(markers,{
        onEachFeature: function (feature, layer) {
            L.marker([feature.geometry.coordinates[0][0][1], feature.geometry.coordinates[0][0][0]]).bindPopup(feature.properties.name);
                if (feature.properties.statlv ==1) {                
                layer.setStyle({fillColor: '#0000FF ', fillOpacity: 1, color: '#0000FF ', weight: 1, opacity: 1});
                }
                else if (feature.properties.statlv ==2) {
                layer.setStyle({fillColor: '#FFFF00 ', fillOpacity: 1, color: '#FFFF00 ', weight: 1, opacity: 1});
                }
                else if (feature.properties.statlv ==3) {
                layer.setStyle({fillColor: '#FF0000 ', fillOpacity: 1, color: '#FF0000 ', weight: 1, opacity: 1});
                }
            }
        })
        .addTo(map);
    map.fitBounds(mark_feature.getBounds(), { padding: [100, 100] });
};
};
