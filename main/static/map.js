const attribution =
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const map = L.map("map");
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: attribution,
}).addTo(map);
map.fitWorld();

const markers = JSON.parse(document.getElementById("markers-data").textContent);

var feature = L.geoJSON(markers,{
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

map.fitBounds(feature.getBounds(), { padding: [100, 100] });
